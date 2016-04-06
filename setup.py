#!/usr/bin/env python
#
# Copyright (c) 2015 Nutanix Inc. All rights reserved.
#
# Author: Anand Nevase <anand.nevase@xoriant.com>
#
# Description: Setup file to manage and create TechX Calculator application
# deliverable


import ConfigParser


from setuptools import setup, find_packages


def prepare_version():
    """
    Method to prepare release version, _build_number will be used for internal purpose
    :return:
    """
    config = ConfigParser.ConfigParser()
    config.read('version.txt')
    section = 'version'
    _major_release = config.getint(section, 'major.release')
    _minor_release = config.getint(section, 'minor.release')
    _point_release = config.getint(section, 'point.release')
    _build_number = config.getint(section, 'build.number')
    if _build_number != 0:
        return "%s.%s.%s.%s" % (_major_release, _minor_release, _point_release, _build_number)
    else:
        return "%s.%s.%s" % (_major_release, _minor_release, _point_release)


tests_require = ['nose == 1.3.7', 'mock == 1.3.0', 'coverage >= 4.0.3']

install_requires = [
    'flask == 0.10.1'
]

setup(
    author='TechX, Inc.',
    name='TechX-Calculator',
    description='TechX Calcualtor for demo CI,CA with Docker,Jenkins',
    version=prepare_version(),
    packages=find_packages(exclude=('unittests', )),
    namespace_packages=['techx'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['calculator = techx.calulator.web.app:run_app']
    },
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='nose.collector',
    zip_safe=False
)
