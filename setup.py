import pathlib
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()


DEVELOPMENT_REQUIREMENTS = ["black", "isort", "pre-commit", "pytest", "pytest-cov", "tox"]


setup(
    name="easy-choices",
    version="0.1.0",
    description="Handle choices field easily",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/olist/easy-choices",
    author="Olist Developers",
    author_email="developers@olist.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable  ",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    extras_require={
        "dev": DEVELOPMENT_REQUIREMENTS,
    },
)
