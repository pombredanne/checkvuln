# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

import os
import sqlite3
import errno
import distutils.version

from checkvuln import exceptions
from checkvuln.containers import Installed


class MacPorts(sqlite3.Connection):
    """
    Class dealing with the SQLite3 registry used by MacPorts
    """
    def __init__(self, database):
        db = os.path.expanduser(database)
        if db != ":memory:" and os.path.isfile(db) != True:
            raise exceptions.FileError(errno.ENOENT, "non-existent db", db)
        super(MacPorts, self).__init__(db)

        # Because pylint has certain issues with C libraries:
        # pylint: disable=E1101
        self.row_factory = self._process_row
        self.create_collation("version", self._version)
        self._cur = self.cursor()
        # pylint: enable=E1101

    def installed(self):
        """
        Retrieve a list of installed ports

        Returns:
            List of named Installed tuples
        """
        self._cur.execute("select name, version, revision from ports")
        return self._cur.fetchall()

    @staticmethod
    def _process_row(cur, row):
        port = {}
        for idx, column in enumerate(cur.description):
            port[column[0]] = row[idx]
        return Installed(**port)

    @staticmethod
    def _version(ver1, ver2):
        v1 = distutils.version.LooseVersion(ver1)
        v2 = distutils.version.LooseVersion(ver2)
        if v1 == v2:
            return 0
        if v1 < v2:
            return -1
        return 1
