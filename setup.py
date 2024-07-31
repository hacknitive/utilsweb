from setuptools import setup, find_packages
from sys import platform
from os.path import exists

# ================================================================================================= LONG_DESCRIPTION
with open("README.md", "r", encoding="utf-8") as handler:
    LONG_DESCRIPTION = handler.read()


# ================================================================================================= VERSION
with open("VERSION", "r", encoding="utf-8") as handler:
    VERSION = handler.read().lstrip('v')


# ================================================================================================= install_requires
def parse_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()


if exists('requirements.txt'):
    install_requires = parse_requirements('requirements.txt')

else:
    if platform.startswith('win'):
        install_requires = parse_requirements('requirements-windows.txt')
    elif platform == 'darwin':
        install_requires = parse_requirements('requirements-macos.txt')
    elif platform.startswith('linux'):
        install_requires = parse_requirements('requirements-linux.txt')

# ==============================================================================
setup(
    name="utilsweb",
    version=VERSION,
    packages=find_packages(),
    install_requires=install_requires,
    author="Reza 'Sam' Aghamohammadi (Hacknitive)",
    author_email="hacknitive@gmail.com",
    description="Create and get real useragent strings",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/hacknitive/utilsweb",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
