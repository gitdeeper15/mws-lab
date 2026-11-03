# Contributing to Morocco_Water_Scarcity

**Water Scarcity in Morocco: A Multivariate Analysis of Climatic, Agricultural, and Socioeconomic Drivers**

---

## Status

This project is a **completed research release** (`1.0.0`). The manuscript,
figures, data, and analysis pipeline are published.

Contributions at this stage are limited to:

- **Corrections**: typos, incorrect references, metadata errors.
- **Reproducibility fixes**: dependency issues, broken scripts.
- **Packaging fixes**: build artifacts, file structure.
- **Documentation clarity**: ambiguities in README or methodology.

**Not accepted at this stage:**

- New analyses that change the reported findings.
- Changes to the OLS specification or indicator definitions.
- Rewriting the manuscript's conclusions.
- New dependencies unless justified as a reproducibility fix.

For extensions (new analyses, sensitivity checks, confirmatory studies),
open an issue first to discuss scope.

---

## Reporting Issues

Open an issue with:

- A one-sentence description.
- The affected file (e.g., `README.md`, `DATA/raw/fetch_worldbank_data.py`).
- A minimal reproduction or screenshot.
- Expected vs. actual behavior.

---

## Submitting Corrections

```bash
git checkout -b fix/short-description
# make changes
git commit -m "fix: short description"
git push origin fix/short-description
```

Then open a pull request. Each PR should address one concern.

---

Code Standards

Language Standard
Python PEP 8, black (88 chars), isort, flake8
Markdown markdownlint (MD013 disabled)
YAML yamllint

Reproducibility: every code change must reproduce the results reported in
PUBLICATION/water_scarcity_morocco.pdf on a clean environment. If a change
alters any reported number (R², coefficients, p-values), it is not a
correction — open an issue to discuss.

---

Data Provenance

Data under DATA/raw/ originates from:

· World Bank WDI — public domain (CC-BY-4.0), see
  .
· Morocco 2025 State of the Environment Report — cited per source terms.

Do not commit derived data that is not reproducible from the scripts in
DATA/raw/. Do not commit personal or sensitive data (none exists in the
current dataset).

---

Review Process

· All changes are reviewed by the maintainer (Samir Baladi).
· Changes to the manuscript, figures, or reported numbers require explicit
  documentation in CHANGELOG.md with rationale.
· After the 1.0.0 release, any change to reported findings would require a
  new version (e.g., 1.1.0) with a new DOI deposit on Zenodo.

---

Contact

· Email: gitdeeper@gmail.com
· ORCID: https://orcid.org/0009-0003-8903-0029
· Zenodo DOI: https://doi.org/10.5281/zenodo.23884236
· PyPI: https://pypi.org/project/mws-lab/
· Figshare: https://doi.org/10.6084/m9.figshare.34884417
· Figshare: https://doi.org/10.6084/m9.figshare.34884417
· Website: https://mws-lab.netlify.app

---

Thank you for helping improve the reproducibility of this research.
