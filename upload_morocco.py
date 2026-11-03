#!/usr/bin/env python3

"""Morocco_Water_Scarcity — PyPI Uploader"""

import requests
import hashlib
import os
import glob
import sys

PACKAGE_NAME = "mws-lab"
VERSION = "1.0.0"
SITE_URL = "https://mws-lab.netlify.app"
ZENODO_DOI = "10.5281/zenodo.23884236"
FIGSHARE_DOI = "10.6084/m9.figshare.34884417"
ORCID_URL = "https://orcid.org/0009-0003-8903-0029"

# Token via environment variable (safer than hardcoding)
TOKEN = os.environ.get("PYPI_TOKEN", "")

if not TOKEN:
    print("❌ PYPI_TOKEN not set.")
    print("   Run: export PYPI_TOKEN='pypi-...'")
    sys.exit(1)

print("=" * 60)
print(f"Morocco_Water_Scarcity v{VERSION} — PyPI Upload")
print("=" * 60)

try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    print(f"README.md: {len(readme)} characters")
except FileNotFoundError:
    readme = (
        "Water Scarcity in Morocco: A Multivariate Analysis of "
        "Climatic, Agricultural, and Socioeconomic Drivers."
    )

wheel_files = glob.glob("dist/*.whl")
tar_files = glob.glob("dist/*.tar.gz")

if not wheel_files and not tar_files:
    print("❌ No distribution files found in dist/")
    sys.exit(1)

print(f"\nFiles:")
for f in wheel_files + tar_files:
    print(f"   • {os.path.basename(f)}")

CLASSIFIERS = [
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
]

upload_success = False
upload_failed = False

for filepath in wheel_files + tar_files:
    filename = os.path.basename(filepath)
    print(f"\nUploading: {filename}")

    if filename.endswith(".tar.gz"):
        filetype = "sdist"
        pyversion = "source"
    else:
        filetype = "bdist_wheel"
        pyversion = "py3"

    with open(filepath, "rb") as f:
        content = f.read()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()

    data_fields = [
        (":action", "file_upload"),
        ("metadata_version", "2.1"),
        ("name", PACKAGE_NAME),
        ("version", VERSION),
        ("filetype", filetype),
        ("pyversion", pyversion),
        ("md5_digest", md5_hash),
        ("sha256_digest", sha256_hash),
        ("description", readme),
        ("description_content_type", "text/markdown"),
        ("author", "Samir Baladi"),
        ("author_email", "gitdeeper@gmail.com"),
        ("license", "MIT"),
        ("summary", (
            "Water Scarcity in Morocco: A Multivariate Analysis of "
            "Climatic, Agricultural, and Socioeconomic Drivers"
        )),
        ("home_page", SITE_URL),
        ("project_urls", (
            f"Homepage, {SITE_URL}\n"
            f"Website, {SITE_URL}\n"
            f"Manuscript, https://doi.org/{ZENODO_DOI}\n"
            f"Zenodo, https://doi.org/{ZENODO_DOI}\n"
            f"Figshare, https://doi.org/{FIGSHARE_DOI}\n"
            f"ORCID, {ORCID_URL}"
        )),
        ("requires_python", ">=3.9"),
        ("keywords", (
            "water scarcity, morocco, world bank indicators, "
            "OLS regression, environmental science, water policy"
        )),
    ]
    for c in CLASSIFIERS:
        data_fields.append(("classifiers", c))

    try:
        with open(filepath, "rb") as f:
            response = requests.post(
                "https://upload.pypi.org/legacy/",
                files={"content": (filename, f, "application/octet-stream")},
                data=data_fields,
                auth=("__token__", TOKEN),
                timeout=90,
                headers={"User-Agent": f"{PACKAGE_NAME}-Uploader/{VERSION}"},
            )

        print(f"   Status: {response.status_code}")

        if response.status_code == 200:
            print("   ✅ SUCCESS")
            upload_success = True
        else:
            print(f"   ❌ Error: {response.text[:400]}")
            upload_failed = True
    except Exception as e:
        print(f"   ❌ Exception: {e}")
        upload_failed = True

print("\n" + "=" * 60)
if upload_success and not upload_failed:
    print(f"✅ {PACKAGE_NAME} v{VERSION} uploaded successfully!")
    print(f"🔗 https://pypi.org/project/{PACKAGE_NAME}/{VERSION}/")
else:
    print(f"❌ Upload failed.")
print("=" * 60)
