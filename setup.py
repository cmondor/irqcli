# coding: utf-8

"""
    IRQ Balancer

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import sys
from setuptools import setup, find_packages

NAME = "cmondor_irq"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["statistics ~= 1.0.3.5"]

setup(
    name=NAME,
    version=VERSION,
    description="IRQ Balancer",
    author_email="chris.mondor@gmail.com",
    url="",
    keywords=["IRQ Balancer"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Library for describing the current distribution of IRQ interrupts per CPU
    and suggestions for balancing.
    """
)
