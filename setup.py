from setuptools import setup

with open("README.md", "r", encoding="utf-8") as handler:
    long_description = handler.read()

setup(
    name="configloader",
    version="1.0.1",
    description="Config Parser and Loader",
    url="https://git.liateam.net/python/packages/configloader.git",
    author="Shahab Ghosni",
    author_email="s.ghosni@liateam.ir",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD 2-clause",
    packages=["configloader"],
    package_dir={"": "."},
    install_requires=[
        "pydantic >= 1.10",
        "packaging >= 23.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
