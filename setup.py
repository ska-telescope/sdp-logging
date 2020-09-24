#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PIP setup script for the SDP Logging package."""

import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='ska-sdp-logging',
    description='SKA standard logging for SDP',
    author='SKA Sim Team',
    license='License :: OSI Approved :: BSD License',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/ska-telescope/sdp-logging',
    package_dir={"": "src"},
    packages=setuptools.find_packages('src'),
    # Workaround: avoid declaring pytango dependency.
    # It's ok to fail to load if not there.
    # install_requires=[
    #     'pytango'
    # ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pylint2junit',
        'pytest',
        'pytest-cov',
        'pytest-json-report',
        'pytest-pycodestyle',
        'pytest-pydocstyle',
        'pytest-pylint'
    ],
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: BSD License"
    ]
)
