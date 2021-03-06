from setuptools import setup

from setuptools import setup
import re

with open("makeapi/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

with open("README.md", "r") as f:
    long_desc = f.read()

setup(
    name="makeapi",
    install_requires=["jinja2"],
    packages=["makeapi"],
    version=version,
    license="MIT",
    url="https://github.com/FrostiiWeeb/makeapi",
    long_description=long_desc,
    long_description_content_type="text/markdown",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="A package to make an API.",  # Give a short description about your library
    author="Alex Hutz",  # Type in your name
    author_email="frostiiweeb@gmail.com",  # Provide either the link to your github or to your website
    keywords=["web"],  # Keywords that define your package best
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
