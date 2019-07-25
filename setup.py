"""A setuptools for MahaDiscom Energy Bill Python bindings

See:
https://github.com/hemantkamalakar/MahaDiscomEnergyBill
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='MahaDiscomEnergyBill',

    version='0.1.0',

    description='A Python API for Mahadiscom energy bill',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/hemantkamalakar/MahaDiscomEnergyBill',

    # Author details
    author='Hemant Kamalakar',
    author_email='hemant.kamalakar@gmail.com',

    # Choose your license
    license='Apache License',

    classifiers=[
        'Intended Audience :: Developers',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

    ],

    # What does your project relate to?
    keywords='Python API for Mahadiscom energy bill',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['requests','json'],

)
