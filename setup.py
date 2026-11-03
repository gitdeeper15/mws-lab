#!/usr/bin/env python3
"""Setup script for Morocco_Water_Scarcity.

Water Scarcity in Morocco:
A Multivariate Analysis of Climatic, Agricultural, and Socioeconomic Drivers.
Scope: Python 3.9+.
Website: https://mws-lab.netlify.app
DOI: 10.5281/zenodo.23884236
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

try:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [
            line.strip()
            for line in fh
            if line.strip() and not line.startswith("#")
        ]
except FileNotFoundError:
    requirements = [
        "pandas>=1.5.0",
        "numpy>=1.23.0",
        "scipy>=1.9.0",
        "statsmodels>=0.13.0",
        "matplotlib>=3.6.0",
        "seaborn>=0.12.0",
        "requests>=2.28.0",
    ]

setup(
    name="mws-lab",
    version="1.0.0",
    author="Samir Baladi",
    author_email="gitdeeper@gmail.com",
    description=(
        "Water Scarcity in Morocco: A Multivariate Analysis of "
        "Climatic, Agricultural, and Socioeconomic Drivers"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(
        exclude=["tests", "tests.*", "docs", "docs.*", "PUBLICATION", "PUBLICATION.*"]
    ),
    include_package_data=True,
    package_data={
        "morocco_water_scarcity": ["data/*.csv", "data/*.json"],
    },
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
        ],
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords=(
        "water scarcity, morocco, world bank indicators, "
        "OLS regression, environmental science, water policy"
    ),
    project_urls={
        "Homepage": "https://mws-lab.netlify.app",
        "Website": "https://mws-lab.netlify.app",
        "PyPI": "https://pypi.org/project/mws-lab/",
        "Figshare": "https://doi.org/10.6084/m9.figshare.34884417",
        "Figshare": "https://doi.org/10.6084/m9.figshare.34884417",
        "Manuscript": "https://doi.org/10.5281/zenodo.23884236",
        "Zenodo": "https://doi.org/10.5281/zenodo.23884236",
        "ORCID": "https://orcid.org/0009-0003-8903-0029",
    },
)
