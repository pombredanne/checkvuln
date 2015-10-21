#!/usr/bin/env python
#
# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

import unittest

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover("test")
    unittest.TextTestRunner().run(suite)
