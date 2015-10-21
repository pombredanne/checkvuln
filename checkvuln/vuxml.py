# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

import os
import re
import xml.etree.ElementTree

from checkvuln import exceptions
from checkvuln.utils import fetch, cmp_version
from checkvuln.containers import Vuln, Range
from checkvuln.packages.defusedxml.ElementTree import parse, DefusedXMLParser


class VuXML(object):
    """
    Class handling the Vulnerability and eXposure Markup Language
    https://vuxml.freebsd.org/

    Attributes:
        vulns: List of Vuln-tuples
    """
    def __init__(self, url, cache, modified, cafile=None):
        self._url = url
        self._cache = os.path.expanduser(cache)
        self._modified = os.path.expanduser(modified)
        self._cafile = cafile and os.path.expanduser(cafile) or None

        self.vulns = []

    def parse(self):
        """
        Parse a VuXML file and store the result in a list of named tuples

        Returns:
            A list of named Vuln-tuples

        Raises:
            FileError: unable to open the VuXML cache
        """
        builder = xml.etree.ElementTree.TreeBuilder(element_factory=Element)
        parser = DefusedXMLParser(target=builder)
        # Note that forbid_dtd isn't passed (defaults to False) due to
        # the vuxml definition being declared.  However, no actual
        # lookups are made.
        try:
            tree = parse(self._cache, parser=parser, forbid_entities=True,
                         forbid_external=True)
        except IOError as e:
            raise exceptions.FileError(e.errno, e.strerror, e.filename)
        root = tree.getroot()

        for vuln in root.iterfind("vuln"):
            # Empty entries contain a tag named 'cancelled', which may
            # refer to another entry with the 'superseded' attribute.
            if vuln.findall("cancelled"):
                continue

            topic = self._topic(vuln)
            description = self._description(vuln)
            references = self._references(vuln)
            for affect in self._affects(vuln):
                self.vulns.append(Vuln(
                    name=affect["name"],
                    range=affect["range"],
                    summary=topic,
                    description=description,
                    references=references
                ))
        return self.vulns

    def audit(self, name, version):
        """
        Audit a specific version of a package

        Args:
            name: Name of the package to audit
            version: Version of the package to audit

        Returns:
            A list of matching Vuln-tuples
        """
        result = []
        for vuln in self.vulns:
            if name != vuln.name:
                continue
            if cmp_version(version, vuln.range):
                result.append(vuln)
        return result

    def fetch(self):
        """
        Download the VuXML file
        """
        fetch(self._url, self._cache, self._modified, cafile=self._cafile)

    @staticmethod
    def close():
        return

    @staticmethod
    def _topic(elem):
        t = elem.find("topic")
        if t is not None:
            t = t.text
        return t

    @staticmethod
    def _description(elem):
        desc = elem.find("description").itertext()
        return "".join([re.sub(r"\n[\s]+", "\n", d) for d in desc])

    @staticmethod
    def _references(elem):
        result = []
        refs = elem.find("references")
        for name in ["cvename", "freebsdsa", "url"]:
            for ref in refs.iterfind(name):
                result.append(ref.text)
        return result

    @staticmethod
    def _affects(elem):
        """
        Flatten the <affects> element, which specifies the vulnerable
        packages and their ranges in a format like

        <affects>
          <package>
            <name>py27-blargh</name>
            <name>py34-blargh</name>
            <range><gt>1.1.1</gt><lt>1.1.10</lt></range>
            <range><gt>1.2.*</gt><lt>1.2.10</lt></range>
            <range><gt>2.0.*</gt><lt>2.0.10</lt></range>
          </package>
          <package>
            <name>py35-blargh</name>
            <range><gt>1.2.2</gt><lt>1.2.6</lt></range>
          </package>
        </affects>
        """
        result = []
        affects = elem.find("affects")
        for package in affects.iterfind("package"):
            for name in package.iterfind("name"):
                for pkgrange in package.iterfind("range"):
                    versions = {}
                    for field in Range._fields:
                        value = pkgrange.find(field)
                        if value is not None:
                            value = value.text
                            # special case for <gt> -- rewrite wildcard
                            # values to help the version comparison
                            # checker, e.g. 1.2.* -> 1.2
                            if field == "gt":
                                value = value.replace(".*", "")
                        versions[field] = value
                    result.append({
                        "name": name.text,
                        "range": Range(**versions)
                    })
        return result


class Element(xml.etree.ElementTree.Element):
    namespaces = {"vuxml": "http://www.vuxml.org/apps/vuxml-1"}

    def __init__(self, *args, **kwargs):
        super(Element, self).__init__(*args, **kwargs)

    def iterfind(self, path, namespaces=None):
        return super(Element, self).iterfind(*self._setup(path, namespaces))

    def findall(self, path, namespaces=None):
        return super(Element, self).findall(*self._setup(path, namespaces))

    def find(self, path, namespaces=None):
        return super(Element, self).find(*self._setup(path, namespaces))

    def _setup(self, path, namespaces):
        if not namespaces:
            path = "vuxml:{}".format(path)
            namespaces = self.namespaces
        return path, namespaces
