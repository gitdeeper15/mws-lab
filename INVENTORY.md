# mws-lab — Complete Inventory

**Version:** 1.0.0
**Release Date:** 2026-11-02
**Series:** mws-lab-01
**Author:** Samir Baladi
**Email:** gitdeeper@gmail.com
**ORCID:** 0009-0003-8903-0029
**License:** MIT (code) · CC-BY-4.0 (docs, manuscript, figures)
**Status:** Published · Exploratory associational analysis · No causal claims
**DOI (Zenodo):** 10.5281/zenodo.23884236
**DOI (OSF Registration):** (Pending)
**DOI (Figshare):** 10.6084/m9.figshare.34884417
**OSF Project:** osf.io/6m9ef

---

## Repository Links

| Platform | URL | Role |
|----------|-----|------|
| GitHub | https://github.com/gitdeeper15/mws-lab | Primary |
| GitLab | https://gitlab.com/gitdeeper15/mws-lab | Mirror |
| Codeberg | https://codeberg.org/gitdeeper15/mws-lab | Mirror |
| Bitbucket | https://bitbucket.org/gitdeeper15/mws-lab | Mirror |
| PyPI | https://pypi.org/project/mws-lab | Python package |
| Zenodo | https://doi.org/10.5281/zenodo.23884236 | DOI (manuscript archive) |
| OSF Project | https://osf.io/6m9ef | Associated project |
| Figshare | https://doi.org/10.6084/m9.figshare.34884417 | Secondary archive |
| Website | https://mws-lab.netlify.app | Live documentation |
| ORCID | https://orcid.org/0009-0003-8903-0029 | Identity |
| GitHub Release | https://github.com/gitdeeper15/mws-lab/releases/tag/v1.0.0 | v1.0.0 |

---

## Root Files

| File | Size | Purpose |
|------|------|---------|
| `.gitignore` | 421 B | Git ignore rules |
| `AUTHORS.md` | 3.67 KB | Contributors |
| `CHANGELOG.md` | 5.17 KB | Version history |
| `CITATION.cff` | 2.18 KB | Citation metadata |
| `CONTRIBUTING.md` | 2.88 KB | Contribution guidelines |
| `INVENTORY.md` | this | Complete inventory |
| `LICENSE` | 4.13 KB | MIT + CC-BY-4.0 |
| `MANIFEST.in` | 421 B | sdist manifest |
| `OSF_REGISTRATION.md` | 24.58 KB | OSF registration record |
| `README.md` | 23.25 KB | Main documentation |
| `VERSION` | 5 B | 1.0.0 |
| `pyproject.toml` | 2.17 KB | Python config |
| `requirements.txt` | 424 B | Python deps |
| `setup.cfg` | 2.19 KB | Setup config |
| `setup.py` | 2.88 KB | Package setup |
| `upload_morocco.py` | 4.52 KB | PyPI uploader |
| `FINAL_REPORT.json` | 2.53 KB | Pipeline execution record |
| `PROJECT_SUMMARY.txt` | 779 B | Project summary |
| `scientific_state.json` | 1.43 KB | Internal scientific state |

---

## Directories

| Directory | Files | Purpose |
|-----------|-------|---------|
| `mws_lab/` | 3 | Python package |
| `DATA/raw/` | 3 | World Bank WDI extract + fetch script |
| `ANALYSIS/` | 2 | Analysis report + insights |
| `PUBLICATION/` | 24 | Manuscript, figures, Netlify, dist |
| `REPORTS/` | 21 | Governance and audit |
| `EXTERNAL_REVIEW/` | 3 | External review record |
| `VALIDATION/` | 1 | Language lock report |
| `docs/` | 2 | Iteration log + audit |

**Total (active):** 82 files · 18 root files · 8 directories

---

## mws_lab/ (Python package)

| File | Purpose |
|------|---------|
| `mws_lab/__init__.py` | Package marker + metadata |
| `mws_lab/fetch.py` | Reproducible WDI fetch script |
| `mws_lab/data/worldbank_data.csv` | WDI extract (16 KB) |
| `mws_lab/data/input.json` | Indicator configuration |

**Console script:** `mws-lab-fetch`

---

## Indicators (5)

| Indicator | Code | Coverage |
|-----------|------|----------|
| Annual freshwater withdrawals | ER.H2O.FWTL.K3 | 2000–2022 |
| Agricultural land irrigated (%) | AG.LND.IRIG.AG.ZS | 2004–2019 |
| Population growth (annual %) | SP.POP.GROW | 2000–2025 |
| Cereal yield (kg/ha) | AG.YLD.CREL.KG | 2000–2024 |
| Arable land (% of land area) | AG.LND.ARBL.ZS | 2000–2024 |

---

## Figures (7)

| Figure | Purpose |
|--------|---------|
| Figure 1 | Conceptual Framework |
| Figure 2 | Methodology Flowchart |
| Figure 3 | Selected Water Indicators |
| Figure 4 | Water Allocation |
| Figure 5 | Rainfall and Reservoir Indicators |
| Figure 6 | Correlation Matrix |
| Figure 7 | OLS Regression Results |

---

## Model Specification (OLS)

```

FW_t = β0 + β1·IRRIG_t + β2·POPGR_t + β3·YIELD_t + β4·ARABLE_t + ε_t

β̂ = (XᵀX)⁻¹ Xᵀy

```

**Estimation window:** 2004–2019 (complete-case, n = 16).

---

## Key Results

| Dimension | Result |
|-----------|--------|
| Model R² | 0.812 (adjusted 0.744) |
| Complete-case sample | n = 16 (2004–2019) |
| Condition number κ(X) | ≈ 78,500 (severe) |
| Agricultural share | ≈ 88% |
| Per-capita decline | ≈2,560 → ≈620 m³ |
| Water-stress index (2022) | 50.75% |

---

## Dependencies

### Python (runtime)

- `pandas ≥ 1.5.0`
- `numpy ≥ 1.23.0`
- `scipy ≥ 1.9.0`
- `statsmodels ≥ 0.13.0`
- `matplotlib ≥ 3.6.0`
- `seaborn ≥ 0.12.0`
- `requests ≥ 2.28.0`

### Python (dev)

- `pytest ≥ 7.0.0`
- `pytest-cov ≥ 4.0.0`
- `black ≥ 23.0.0`
- `flake8 ≥ 6.0.0`
- `isort ≥ 5.12.0`
- `build`
- `twine`

---

## Completion Summary

```

Project: mws-lab — Water Scarcity in Morocco v1.0.0
Status: Published · Exploratory associational analysis · No causal claims
Files: 82 active files (18 root + 64 in subdirectories)
Directories: 8
Indicators: 5 (World Bank WDI)
Figures: 7
Model: OLS, complete-case n = 16 (2004–2019)
R²: 0.812 (adjusted 0.744)
κ(X): ≈ 78,500 (severe multicollinearity)
Causal claims: None (associational only)
License: MIT (code) + CC-BY-4.0 (manuscript, figures, docs)

```

---

## Citation

```bibtex
@software{baladi2026mws_zenodo,
  author = {Baladi, Samir},
  title = {{Water Scarcity in Morocco}: A Multivariate Analysis of
                  Climatic, Agricultural, and Socioeconomic Drivers},
  year = {2026},
  month = nov,
  version = {1.0.0},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.23884236},
  url = {https://doi.org/10.5281/zenodo.23884236},
  note = {Ronin Institute / Rite of Renaissance. Exploratory associational analysis.}
}
```

---

Generated: 2026-11-03
Inventory Version: 1.0.0
Series: mws-lab-01
