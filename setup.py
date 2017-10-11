#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

def get_reqs(requirement_file):
    from pip.req import parse_requirements
    requirements = list(parse_requirements(requirement_file, session='hack'))
    return [str(r.req) for r in requirements]


install_requires = []
test_requires = get_reqs('requirements_dev.txt')
# for running pytest as `python setup.py test`, see
# http://doc.pytest.org/en/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner
setup_requires = ['pytest-runner']

setup(
    name='gunicorn_logstash_formatter',
    version='0.1.0',
    description="A log formatter for gunicorn's access logs to output logstash JSON.",
    long_description=readme + '\n\n' + history,
    author='Government Digital Service',
    url='https://github.com/alphagov/gunicorn-logstash-formatter',
    packages=find_packages(include=['gunicorn_logstash_formatter']),
    include_package_data=True,
    install_requires=install_requires,
    license="MIT license",
    zip_safe=False,
    keywords='gunicorn_logstash_formatter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requires,
    setup_requires=setup_requires,
)
