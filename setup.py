#!/usr/bin/env python3

from setuptools import setup


setup(
    name='fuo_TEMPLATE',
    version='0.1.dev0',
    description='feeluown TEMPLATE plugin',

    # author='feeluown',
    # author_email='feeluown@feeluown.org',

    # packages=[
    #     'fuo_TEMPLATE',
    # ],
    py_modules=['fuo_TEMPLATE'],
    url='https://github.com/feeluown/feeluown-TEMPLATE',
    keywords=['feeluown', 'plugin', 'TEMPLATE'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'feeluown>=3.7.11',
    ],
    entry_points={
        'fuo.plugins_v1': [
            'TEMPLATE = fuo_TEMPLATE',
        ]
    },
)