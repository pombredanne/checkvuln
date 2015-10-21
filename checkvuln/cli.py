# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

import os
import sys
import argparse
import sqlite3

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from checkvuln import __version__, exceptions
from checkvuln.vuxml import VuXML
from checkvuln.macports import MacPorts

WORKERS = {
    "remote": {
        "remote.vuxml": VuXML
    },
    "local": {
        "local.macports": MacPorts
    }
}


class Run(configparser.RawConfigParser):  # pylint: disable=too-many-ancestors
    def __init__(self, verbose, *args, **kwargs):
        self._verbose = verbose
        self._instances = {}
        configparser.RawConfigParser.__init__(self, *args, **kwargs)

    def remote(self, offline=False):
        """
        Initialize remote workers

        Args:
            offline: whether to (re-)fetch vulnerability definitions
        """
        for section, worker in WORKERS["remote"].items():
            if not self.has_section(section):
                continue
            self._debug("initializing {}", section)
            kwargs = dict(self.items(section))
            instance = self._instance(section, worker, **kwargs)
            if not offline:
                self._info("fetching {} -- this may take a while...", section)
                try:
                    instance.fetch()
                except exceptions.FileError as e:
                    self._error("unable to open {}", e.filename)
                    self._error("{} [errno {}]", e.strerror, e.errno)
                    sys.exit(1)
                except exceptions.CertificateError as e:
                    self._error("certificate error for {}", kwargs["url"])
                    sys.exit(1)
            try:
                instance.parse()
            except exceptions.FileError as e:
                self._error("unable to open {}", e.filename)
                self._error("{} [errno {}]", e.strerror, e.errno)
                sys.exit(1)

    def local(self, fmt=None):
        """
        Initialize local workers and audit installed packages against
        configured remotes

        Args:
            fmt: format string used in the output of vulnerable packages
        """
        if not fmt:
            try:
                fmt = self.get("output", "fmt")
            except (configparser.NoSectionError, configparser.NoOptionError):
                fmt = "{name}-{version}: {summary}"

        for section, worker in WORKERS["local"].items():
            if not self.has_section(section):
                continue
            self._debug("initializing {}", section)
            kwargs = dict(self.items(section))
            remotes = kwargs["remote"]
            del kwargs["remote"]
            local_ins = self._instance(section, worker, **kwargs)
            installed = local_ins.installed()

            for r in [r.strip() for r in remotes.split(",")]:
                self._debug("{}: auditing with {}", section, r)
                remote_ins = self._instances[r]
                for has in installed:
                    for vuln in remote_ins.audit(has.name, has.version):
                        v = vuln._asdict()
                        # vulnerability tuples specifies a range of
                        # vulnerable versions, rather than a specific
                        # one.  also, names may not match due to naming
                        # translations, hence:
                        v.update(has._asdict())
                        try:
                            self._warn(fmt, **v)
                        except KeyError:
                            self._error("invalid format: {}", fmt)
                            self._error("available: {}", ", ".join(v.keys()))
                            sys.exit(1)

    def load(self, filename):
        """
        Load a configuration file

        Args:
            filename: file to read
        """
        try:
            with open(filename) as f:
                self.readfp(f)
        except IOError:
            self._error("no config found at {}", filename)
            sys.exit(1)

    def close(self):
        """
        Clean up worker instances
        """
        for instance in self._instances.values():
            instance.close()

    def _instance(self, name, cls, **kwargs):
        try:
            instance = cls(**kwargs)
        except TypeError as e:
            self._error("incomplete configuration for {}", name)
            self._error("exception: {}", e)
            sys.exit(1)
        except exceptions.FileError as e:
            self._error("{} {} [errno {}]", e.strerror, e.filename, e.errno)
            sys.exit(1)
        except sqlite3.OperationalError:
            self._error("invalid configuration for {}", name)
            self._error("unable to open database {}", kwargs["database"])
            sys.exit(1)
        self._instances[name] = instance
        return instance

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def _debug(self, fmt, *args, **kwargs):
        if not self._verbose:
            return
        msg = "DEBUG: {}\n".format(fmt)
        sys.stdout.write(msg.format(*args, **kwargs))

    @staticmethod
    def _info(fmt, *args, **kwargs):
        fmt += "\n"
        sys.stdout.write(fmt.format(*args, **kwargs))

    @staticmethod
    def _warn(fmt, *args, **kwargs):
        fmt += "\n"
        sys.stdout.write(fmt.format(*args, **kwargs))

    @staticmethod
    def _error(fmt, *args, **kwargs):
        msg = "ERROR: {}\n".format(fmt)
        sys.stderr.write(msg.format(*args, **kwargs))


def main():
    args = parse_args()

    with Run(args.verbose) as run:
        run.load(os.path.expanduser(args.config))
        run.remote(args.offline)
        run.local(args.fmt)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("-c", "--config", default="~/.checkvuln/checkvuln.cfg")
    p.add_argument("-f", "--fmt")
    p.add_argument("-o", "--offline", action="store_true")
    p.add_argument("-v", "--verbose", action="store_true")
    p.add_argument("--version", action="version",
                   version="%(prog)s " + __version__)
    args = p.parse_args()

    return args
