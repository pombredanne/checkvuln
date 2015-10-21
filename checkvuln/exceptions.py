# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

try:
    from urllib import request
except ImportError:
    import urllib2 as request


class ReadError(Exception):
    pass


class FileError(IOError):
    pass


class CertificateError(request.URLError):
    pass
