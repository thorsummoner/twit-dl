#!/usr/bin/env python3
""" twit-dl
"""
import setuptools

setuptools.setup(
    name='twit-dl',
    version='0.1.0dev1',
    description=__doc__,
    url='https://github.com/thorsummoner/twit-dl',
    author='Dylan Scott Grafmyre',
    author_email='dylan.grafmyre@gmail.com',

    packages=['twitter_dl'],

    install_requires=['twitter-scraper'],

    entry_points={
        'console_scripts': [
            'twit-dl=twitter_dl.__main__:main',
        ],
    },
)
