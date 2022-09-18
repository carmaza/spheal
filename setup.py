# Distributed under the MIT License.
# See LICENSE for details.

from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name='sphrids',
    version='0.1.0',
    description="Particle spherical distributions.",
    long_description=long_description,
    url='https://github.com/carmaza/sphrdis',
    author='Cristóbal Armaza',
    author_email='ca455@cornell.edu',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    keywords='spherical',
    packages=find_packages(),
    install_requires=['matplotlib>=3.5.3', 'numpy>=1.23.0'],
    python_requires='>=3.8')
