# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

import unittest

try:
    from io import StringIO, BytesIO
except ImportError:
    from StringIO import StringIO
    from cStringIO import StringIO as BytesIO

from checkvuln import exceptions
from checkvuln.utils import fetch


class FetchTests(unittest.TestCase):
    def test_304(self):
        kwargs = {
            "url": "https://svn.freebsd.org/index.html",
            "cafile": None,
            "dst_content": BytesIO(),
            "dst_modified": StringIO(),
        }

        # This will obviously fail whenever the content is updated
        # between the calls
        fetch(**kwargs)
        kwargs["dst_modified"].seek(0)
        self.assertEqual(fetch(**kwargs), 304)

    def test_max_size(self):
        kwargs = {
            "url": "https://svn.freebsd.org/index.html",
            "cafile": None,
            "dst_content": BytesIO(),
            "dst_modified": StringIO(),
            "max_size": 1,
        }

        with self.assertRaises(exceptions.ReadError):
            fetch(**kwargs)
