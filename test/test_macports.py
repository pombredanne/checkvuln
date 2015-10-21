# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

import unittest

from checkvuln.macports import MacPorts
from checkvuln.vuxml import VuXML


class MacPortsTests(unittest.TestCase):
    def test_registry(self):
        mp = MacPorts(":memory:")
        with open("test/test_macports.sql") as f:
            mp.executescript(f.read())
        installed = mp.installed()
        self.assertEqual(len(installed), 20)

        vuxml = VuXML(url="", cache="test/test_vuxml.xml", modified="")
        vuxml.parse()
        vulns = []
        for port in installed:
            vulns += vuxml.audit(port.name, port.version)
        self.assertEqual(len(vulns), 4)

        mp.close()
