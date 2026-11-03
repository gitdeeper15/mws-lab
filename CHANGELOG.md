# Morocco_Water_Scarcity — Changelog

All notable changes to this research project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2026-11-02

### Initial Research Release

First public research release of **Water Scarcity in Morocco: A Multivariate
Analysis of Climatic, Agricultural, and Socioeconomic Drivers**.

This release includes the full manuscript, seven figures, the World Bank data
extract, the analysis pipeline, the Python build artifacts, and the project
website. The analysis is **exploratory and associational**; no causal claims
are made.

### Added — Research Manuscript

- `PUBLICATION/water_scarcity_morocco.pdf` — full manuscript (1.3 MB).
- `PUBLICATION/credit_table.md` — CRediT contributor roles.
- Abstract, methodology, results, limitations, and policy implications
  covering Morocco's freshwater trajectory from 2000 to 2025.

### Added — Figures (7)

- `PUBLICATION/figures/Figure_1_Conceptual_Framework.png`
- `PUBLICATION/figures/Figure_2_Methodology_Flowchart.png`
- `PUBLICATION/figures/Figure_3_Selected_Water_Indicators.png`
- `PUBLICATION/figures/Figure_4_Water_Allocation.png`
- `PUBLICATION/figures/Figure_5_Rainfall_and_Reservoir_Indicators.png`
- `PUBLICATION/figures/Figure_6_Correlation_Matrix.png`
- `PUBLICATION/figures/Figure_7_OLS_Regression_Results.png`

### Added — Data

- `DATA/raw/worldbank_data.csv` — World Bank WDI extract (16 KB).
- `DATA/raw/fetch_worldbank_data.py` — reproducible data-fetch script.
- `DATA/raw/input.json` — indicator configuration.

### Added — Analysis

- `ANALYSIS/ANALYSIS_REPORT.md` — analysis summary.
- `ANALYSIS/analysis_insights.json` — structured insights.
- OLS regression with full diagnostics (VIF, condition number, CIs).
- Pairwise Pearson correlation matrix.
- Descriptive statistics and trend summaries.

### Added — Publication Artifacts

- `PUBLICATION/Netlify/` — project website
  (`index.html`, `dashboard.html`, `documentation.html`, `reports.html`,
  `assets/style.css`, `project.json`).
- `PUBLICATION/dist/` — Python package artifacts
  (`morocco-water-scarcity-1.0.0-py3-none-any.whl`,
  `morocco-water-scarcity-1.0.0.tar.gz`).
- `PUBLICATION/manifest.json`, `PUBLICATION/output_summary.txt`.
- `PUBLICATION/ste_website_steering.json`, `PUBLICATION/netlify.toml`.

### Added — Governance and Audit

- `EXTERNAL_REVIEW/` — external review record (2026-11-02).
- `REPORTS/dpia_report.md`, `REPORTS/dpia_report.json` — data protection
  impact assessment.
- `REPORTS/compliance_audit_report.json`.
- `REPORTS/citation_report.md`, `REPORTS/reference_alignment_report.json`,
  `REPORTS/reference_audit_report.json`, `REPORTS/reference_resolver_report.json`.
- `REPORTS/evaluation_report.json`, `REPORTS/feedback_report.json`.
- `REPORTS/results_consistency_report.json`, `REPORTS/review_sync_report.json`.
- `VALIDATION/.lock/language_lock_report.json`.

### Added — Documentation

- `README.md` — full project overview (460 lines, 8 badges).
- `AUTHORS.md` — author and contributor record.
- `CITATION.cff` — citation metadata with Zenodo DOI and ORCID.
- `CHANGELOG.md` — this file.
- `CONTRIBUTING.md` — contribution guidelines.
- `LICENSE` — MIT (code) and CC-BY-4.0 (manuscript, figures, documentation).
- `docs/ITERATION_LOG.md` — iteration history.
- `docs/comprehensive_audit_report.json` — consolidated audit.

### Added — Project Infrastructure

- `VERSION` — `1.0.0`.
- `requirements.txt` — Python dependencies.
- `pyproject.toml` — project metadata.
- `MANIFEST.in` — distribution manifest.
- `.gitignore` — standard Python/OS/IDE ignores.
- `FINAL_REPORT.json` — pipeline execution record (70 agents).
- `scientific_state.json` — internal scientific state record.

### Status

| Dimension | Status |
|-----------|--------|
| Manuscript | Complete (PDF) |
| Figures | 7 included |
| Data | World Bank WDI (5 indicators) |
| Analysis | OLS with diagnostics |
| Sample | n = 16 (model sample) |
| Model R² | 0.812 |
| Package | Built (`dist/`) |
| Website | Built (Netlify) |
| Quality gate | PASSED |
| Causal claims | None (associational) |
| External review | Completed (2026-11-02) |

---

## Roadmap

### 1.0.1 — Maintenance

- Fix any packaging issues discovered post-release.
- Correct typos or metadata inconsistencies.
- Update DOI if re-published on Zenodo.

### 1.1.0 — Extended Analysis (planned)

- Extend the sample beyond 2000–2025 if new data becomes available.
- Sensitivity analysis across alternative indicator definitions.
- Supplementary figures for policy scenarios.

### 2.0.0 — Confirmatory Study (planned)

- Pre-registered design.
- Causal identification strategy (e.g., panel methods or natural experiments).
- External replication dataset.

---

## Notes on the Changelog

- Substantive changes only.
- Any change to the analysis protocol after release is recorded as an
  amendment with explicit rationale.
- Numeric thresholds and diagnostic cutoffs follow standard practice
  (e.g., VIF, condition number) and are not tuned to results.

---

**Last Updated:** 2026-11-02
**Current Version:** 1.0.0
