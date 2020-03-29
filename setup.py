# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in administrative_correspondence/__init__.py
from administrative_correspondence import __version__ as version

setup(
	name='administrative_correspondence',
	version=version,
	description='kamal',
	author='kamal',
	author_email='kamalghanima123@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
