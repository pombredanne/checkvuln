
checkvuln
=========

The purpose of `checkvuln` is to audit installed software against a
number of vulnerability databases.


Package managers
----------------

`checkvuln` is currently compatible with MacPorts_.


Vulnerability databases
-----------------------

`checkvuln` is currently compatible with the `Vulnerability and eXposure
Markup Language`_ (VuXML) list managed by the `FreeBSD project`_.
Unlike a lot of distributors of OSS, the VuXML_ list is kept up-to-date
regardless of whether or not a fix exist, which has the benefit of
lowering the delay of when the end-user is informed.


Installation
------------

Use setup.py::

    $ python setup.py install


Usage
-----

Example configuration (`~/.checkvuln/checkvuln.cfg`)::

    [output]
    fmt = {name}-{version}: {summary}

    [remote.vuxml]
    url = https://svn.freebsd.org/ports/head/security/vuxml/vuln.xml
    cafile = ~/.checkvuln/cafile.pem
    cache = ~/.checkvuln/vuxml.xml
    modified = ~/.checkvuln/vuxml.mod

    [local.macports]
    database = /opt/local/var/macports/registry/registry.db
    remote = remote.vuxml


And run checkvuln::

    $ checkvuln
    fetching remote.vuxml -- this may take a while..
    libxml2-2.9.2: libxml2 -- Enforce the reader to run in constant memory
    openssl-1.0.2: openssl -- multiple vulnerabilities
    python27-2.7.6: Python -- buffer overflow in socket.recvfrom_into()
    sqlite3-3.8.8.3: sqlite -- multiple vulnerabilities


Compatibility
-------------

Works with python 3.x and 2.7.10


License
-------

`BSD 2-Clause`_.


.. _Vulnerability and eXposure Markup Language:
.. _VuXML: https://vuxml.freebsd.org/
.. _FreeBSD Project: https://www.freebsd.org/
.. _MacPorts: https://www.macports.org/
.. _BSD 2-Clause: https://opensource.org/licenses/BSD-2-Clause
