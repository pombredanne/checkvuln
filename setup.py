# Copyright (c) 2015 Hans Jerry Illikainen
#
# Released under the 2-clause BSD license.
# See LICENSE for details.

import shutil
import os
from distutils.core import setup

from checkvuln import __version__

with open("README.rst") as f:
    long_description = f.read()

if not os.path.isdir("build"):
    os.mkdir("build")
    shutil.copy2("checkvuln.py", "build/checkvuln")

setup(
    name="checkvuln",
    version=__version__,
    description="Vulnerability scanner",
    long_description=long_description,
    url="https://github.com/dyntopia/checkvuln",
    license="BSD",
    author="Hans Jerry Illikainen",
    author_email="hji@dyntopia.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Security",
        "Topic :: System :: Systems Administration"
    ],
    packages=[
        "checkvuln",
        "checkvuln.packages",
        "checkvuln.packages.defusedxml",
    ],
    scripts=["build/checkvuln"],
)
