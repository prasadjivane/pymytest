from setuptools import setup, find_packages

setup(
    name='pytestapi',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'pytestapi = pytestapi.tester_cli:main',
        ],
    },
    author='Prasad Jivane',
    author_email='prasadjivane@gmail.com',
    description='Python package that allows you to test APIs from the command line',
    url='https://github.com/prasadjivane/pytestapi',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)
