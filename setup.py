"""This file contains your country package's metadata and dependencies."""

from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="fiscalsim-us",
    version="0.0.3",
    author="Center for Growth and Opportunity at Utah State University (CGO)",
    author_email="fiscalsim@thecgo.org",
    long_description=readme,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    description="FiscalSim federal and state tax and benefit system for the US",
    keywords="tax benefit microsimulation fiscal state household personal",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    url="https://github.com/TheCGO/fiscalsim-us",
    include_package_data=True,  # Will read MANIFEST.in
    data_files=[
        (
            "share/openfisca/openfisca-country-template",
            ["CHANGELOG.md", "LICENSE", "README.md"],
        ),
    ],
    install_requires=[
        "click==8.1.3",
        "h5py",
        "microdf_python",
        "pandas",
        "pathlib",
        "policyengine-core==1.12.1",
        "pytest==5.4.3",
        "pytest-dependency",
        "pyyaml",
        "requests",
        "synthimpute",
        "tables",
        "tabulate",
        "tqdm",
    ],
    extras_require={
        "dev": [
            "autopep8",
            "black",
            "coverage",
            "furo",
            "jupyter-book",
            "jupyter",
            "linecheck",
            "markupsafe",
            "plotly",
            "setuptools",
            "sphinx",
            "sphinx-argparse",
            "sphinx-math-dollar",
            "wheel",
            "yaml-changelog",
        ],
    },
    # Windows CI requires Python 3.9.
    python_requires=">=3.7,<3.10",
    entry_points={
        "console_scripts": [
            "fiscalsim-us = fiscalsim_us.tools.cli:main",
        ],
    },
    packages=find_packages(),
)
