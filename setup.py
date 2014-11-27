#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='s3_storage',
    version='0.1',
    description='Extension for django-storages AWS S3 to specify MEDIA_ROOT for uploaded files and STATIC_ROOT for static files',
    author='Gilang Chandrasa',
    author_email='gilang.chandrasa@gmail.com',
    url='https://github.com/gchandrasa/django-s3-storage',
    packages=[
        's3_storage',
    ],
    install_requires=['django-storages', 'boto'],
)
