#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for openeo_udf.

    This file was generated with PyScaffold 3.0.2.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

import sys
from setuptools import setup

# Add here console scripts and other entry points in ini-style format
entry_points = """
[console_scripts]
# script_name = openeo_udf.module:function
# For example:
# fibonacci = openeo_udf.skeleton:run_json_user_code
"""


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['pyscaffold>=3.0a0,<3.1a0'] + sphinx,
          entry_points=entry_points,
          use_pyscaffold=True,
          scripts=['scripts/run_udf_server',
                   'scripts/execute_udf'])


if __name__ == "__main__":
    setup_package()
