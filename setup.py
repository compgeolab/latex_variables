# Copyright (c) 2021 Santiago Soler
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""
Build and install the package.

Uses setuptools-scm to manage version numbers using git tags.
"""
from setuptools import setup, find_packages


NAME = "latex_variables"
FULLNAME = "Latex Variables"
AUTHOR = "Santiago R. Soler"
AUTHOR_EMAIL = "santiago.r.soler@gmail.com"
MAINTAINER = "Santiago Soler"
MAINTAINER_EMAIL = AUTHOR_EMAIL
LICENSE = "BSD License"
URL = "https://github.com/compgeolab/latex_variable"
DESCRIPTION = "Convert Python variables to LaTeX variables"
KEYWORDS = ""
with open("README.rst") as f:
    LONG_DESCRIPTION = "".join(f.readlines())
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development :: Libraries",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3 :: Only",
    "License :: OSI Approved :: {}".format(LICENSE),
]
PLATFORMS = "Any"
PACKAGES = find_packages(exclude=["doc"])
SCRIPTS = []
PACKAGE_DATA = {}
INSTALL_REQUIRES = []
PYTHON_REQUIRES = ">=3.6"

# Configuration for setuptools-scm
SETUP_REQUIRES = ["setuptools_scm"]
USE_SCM_VERSION = {
    "relative_to": __file__,
    "local_scheme": "node-and-date",
}


if __name__ == "__main__":
    setup(
        name=NAME,
        fullname=FULLNAME,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        use_scm_version=USE_SCM_VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        license=LICENSE,
        url=URL,
        platforms=PLATFORMS,
        scripts=SCRIPTS,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        classifiers=CLASSIFIERS,
        keywords=KEYWORDS,
        install_requires=INSTALL_REQUIRES,
        python_requires=PYTHON_REQUIRES,
        setup_requires=SETUP_REQUIRES,
    )
