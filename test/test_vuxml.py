# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

import unittest

from checkvuln.vuxml import VuXML


class VuXMLTests(unittest.TestCase):
    def test_parse(self):
        vuxml = VuXML(url="", cache="test/test_vuxml.xml", modified="")
        vulns = vuxml.parse()
        self.assertEqual(len(vulns), 60)

    def test_vuln(self):
        vuxml = VuXML(url="", cache="test/test_vuxml.xml", modified="")
        vuxml.parse()
        self.assertEqual(len(vuxml.audit("apache", "2.2.0")), 1)
        self.assertEqual(len(vuxml.audit("otrs", "3.2")), 0)
        self.assertEqual(len(vuxml.audit("otrs", "3.2.0b")), 1)
        self.assertEqual(len(vuxml.audit("otrs", "3.2.0")), 1)
        self.assertEqual(len(vuxml.audit("otrs", "5.0")), 1)
        self.assertEqual(len(vuxml.audit("otrs", "4.0.12")), 2)
        self.assertEqual(len(vuxml.audit("otrs", "4.0.13")), 0)
