# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

import os
import operator
import distutils.version

try:
    from urllib import request
except ImportError:
    import urllib2 as request

from checkvuln import exceptions
from checkvuln.containers import Range


def cmp_version(version, version_range):
    """
    Compare a version against a range of versions

    Args:
        version: target version
        version_range: Range tuple of versions to compare the target with

    Returns:
        True if every specified version in the range matches the target,
        False otherwise
    """
    version = distutils.version.LooseVersion(version)
    for field_operator in Range._fields:
        field_version = getattr(version_range, field_operator)
        if field_version:
            field_version = distutils.version.LooseVersion(field_version)
            opr = getattr(operator, field_operator)
            if not opr(version, field_version):
                return False
    return True


def fetch(url, dst_content, dst_modified, max_size=1024*1024*10, cafile=None):
    """
    Download a specified url

    If the content has changed since the last request, it is written to
    dst_content, and the Last-Modified header is stored in dst_modified

    Args:
        url: url to download
        dst_content: filename or stream for the content
        dst_modified: filename or stream for the Last-Modified header
        max_size: optional: maximum number of bytes to read
        cafile: optional: certificate to validate HTTPS connections against

    Returns:
        HTTP status code

    Raises:
        FileError: unable to open the cafile
        CertificateError: unable to verify the url
    """
    modified = _get_modified(dst_modified)
    req = request.Request(url, headers={"If-Modified-Since": modified})
    try:
        res = request.urlopen(req, cafile=cafile)
    except request.HTTPError as e:
        if e.code == 304:
            return e.code
        raise
    except request.URLError as e:
        if str(e.reason).startswith("[SSL: CERTIFICATE_VERIFY_FAILED]"):
            raise exceptions.CertificateError(e)
        raise request.URLError(e)
    except IOError as e:
        raise exceptions.FileError(e.errno, e.strerror, cafile)
    code = res.getcode()

    _write_content(dst_content, res, max_size)
    _write_modified(dst_modified, res.headers.get("Last-Modified", ""))
    res.close()

    return code


def _get_modified(src):
    modified = ""
    if isinstance(src, str):
        if os.path.isfile(src):
            with open(src) as f:
                modified = f.read()
    else:
        modified = src.read()

    return modified


def _write_modified(dst, modified):
    if not modified:
        return

    if hasattr(modified, "decode"):
        modified = modified.decode("utf-8")

    if isinstance(dst, str):
        fd = os.open(dst, os.O_CREAT | os.O_WRONLY, 0o600)
        fobj = os.fdopen(fd, "w")
        fobj.write(modified)
        fobj.close()
    else:
        dst.write(modified)


def _write_content(dst, src, max_size):
    if isinstance(dst, str):
        fd = os.open(dst, os.O_CREAT | os.O_WRONLY, 0o600)
        fobj = os.fdopen(fd, "wb")
        close = True
    else:
        fobj = dst
        close = False

    read_size = 4096
    total_size = 0
    while True:
        total_size += read_size
        if total_size >= max_size:
            if close:
                fobj.close()
                os.unlink(dst)
            msg = "Too much data ({} >= {})".format(total_size, max_size)
            raise exceptions.ReadError(msg)
        data = src.read(read_size)
        if not data:
            break
        fobj.write(data)

    if close:
        fobj.close()
