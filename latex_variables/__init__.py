# Copyright (c) 2021 Santiago Soler.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
# pylint: disable=missing-docstring,import-outside-toplevel
# Import functions/classes to make the public API
from . import version
from .conversions import to_latex

# Get the version number through setuptools-scm
__version__ = version.version
