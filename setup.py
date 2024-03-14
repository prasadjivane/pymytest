from setuptools import setup, find_packages

setup(
    name="pymytest",
    version="0.7",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "pymytest = pymytest.tester_cli:main",
        ],
    },
    author="Prasad Jivane",
    author_email="prasadjivane@gmail.com",
    description="Python package that allows you to test APIs from the command line",
    url="https://github.com/prasadjivane/pymytest",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
