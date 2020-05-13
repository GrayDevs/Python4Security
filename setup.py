from setuptools import setup, find_packages

setup(
    name='python4Security',
    version='2.1.11',
    description='Searches through git repositories for high entropy strings, digging deep into commit history.',
    url='https://github.com/GrayDevs/Python4Security',
    authors='Zakaria DJAZARI, Antoine PINON',
    license='GNU',
    packages=['python4Security'],
    install_requires=[
		#
    ],
    entry_points = {
      'console_scripts': ['python4Security = Python4Security.python4Security:main'],
    },
)
