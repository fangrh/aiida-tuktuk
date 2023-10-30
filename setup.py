#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="aiida-tuktuk",
    author_email='ruihuanfang@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="The Python package offers a collection of unofficial yet useful tools for managing AiiDA data. As like the Tuk-Tuk: not officially recognized, but quite effective in providing assistance.",
    entry_points={
        'console_scripts': [
            'aiida_tuktuk=aiida_tuktuk.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='aiida_tuktuk',
    name='aiida_tuktuk',
    packages=find_packages(include=['aiida_tuktuk', 'aiida_tuktuk.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/fangrh/aiida_tuktuk',
    version='0.1.0',
    zip_safe=False,
)
