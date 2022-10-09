from setuptools import find_packages, setup

setup(
    name="ServerOcelot",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'serverocelot = mypkg.mymodule:some_func',
        ]
    }
)