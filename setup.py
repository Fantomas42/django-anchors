"""Setup script for django-anchors"""
import os

from setuptools import setup
from setuptools import find_packages

import anchors

setup(
    name='django-anchors',
    version=anchors.__version__,

    description=('A usefull and incredible Django application '
                 'that allow you to stylish anchors in your templates :)'),
    long_description=open(os.path.join('README.rst')).read(),
    keywords='django, anchors, links',

    author=anchors.__author__,
    author_email=anchors.__email__,
    url=anchors.__url__,

    license=anchors.__license__,

    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['anchors.demo']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    install_requires=['beautifulsoup4']
)
