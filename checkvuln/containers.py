# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

from collections import namedtuple

Vuln = namedtuple("Vuln", "name, range, summary, description, references")
Range = namedtuple("Range", "eq, lt, le, gt, ge")
Installed = namedtuple("Installed", "name, version, revision")
