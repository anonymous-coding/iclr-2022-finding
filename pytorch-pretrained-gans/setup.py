#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pytorch_pretrained_gans',
    version='0.0.1',
    description='Project',
    author='Anonymous',
    author_email='',
    url='https://example.com/',
    install_requires=[],
    packages=find_packages(),
    package_data={'pytorch_pretrained_gans': 
        [
            'BigBiGAN/model/weights',
            'StudioGAN/configs',
        ]
    },
)
