#!/usr/bin/env python

from setuptools import setup

setup(name='python_package_example',
      version='0.1',
      description='An example for the python packaging framework',
      author='Daniel Kahlenberg',
      author_email='yourname@msp.com',
      packages=['python_package_example'],
      package_dir={'': 'src'},
      #~ package_data={
	  #~ ...
	  #~ TODO http://lmgtfy.com/?q=python+setuptools+setup.py+%22package_data%3D%22
      include_package_data=True,
      install_requires=[
            'setuptools',
            'pyproj >= 1.8, < 1.9',
            'GDAL >= 1.6, < 1.7'
      ],
      entry_points=("""
          [console_scripts]
          base_run=python_package_example:base_command
          do_osgeo=python_package_example:osgeo_run
          do_pyproj=python_package_example:pyproj_run
          """)
      )
