from setuptools import setup

setup(
    name='grannysmith',
    version='0.1',
    url='https://github.com/donny/grannysmith',
    author='Donny Kurniawan',
    packages=['grannysmith'],
    install_requires=[
        'click',
        'requests'
    ],
    entry_points={
        'console_scripts': ['grannysmith=grannysmith.command_line:main']
    }
)
