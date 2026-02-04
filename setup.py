from setuptools import setup, find_packages

setup(
    name='thought',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'thought=myapp.cli2:main',  # command=module:function
        ],
    },
)