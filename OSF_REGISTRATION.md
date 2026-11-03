# mws-lab — Water Scarcity in Morocco: A Multivariate Analysis of Climatic, Agricultural, and Socioeconomic Drivers

---

**Registration DOI:** (Pending — OSF registration in progress)
**Registration Type:** OSF Preregistration
**Registry:** OSF Registries
**Date Created:** Nov 3, 2026, 4:04 AM
**Date Registered:** Nov 3, 2026, 4:04 AM
**Associated Project:** [https://osf.io/6m9ef](https://osf.io/6m9ef)
**Internet Archive:** (Pending)
**License:** CC-By Attribution 4.0 International
**Contributor:** Samir Baladi

---

## Data / Analytic Code / Materials / Papers / Supplements

The following files were attached to this registration:

- `water_scarcity_morocco.pdf` (1.3 MB)
- `README.md` (23.8 kB)

---

## Overview

### Research questions or hypotheses

RQ1: What are the relative associations between national freshwater withdrawals in Morocco (2000–2025) and four candidate drivers: irrigated land share, population growth rate, cereal yield, and arable land share?

RQ2: Does an OLS model specified on the complete-case window (2004–2019, n = 16) achieve stable and interpretable coefficient estimates given the observed collinearity structure among predictors?

RQ3: What do the strength and structure of the observed associations imply for water policy priorities in Morocco?

Note: All three questions are framed as exploratory and associational. No causal hypotheses are specified. The design does not support causal identification.

### Foreknowledge of data or evidence

Analyses in this plan have been conducted already. At least some of the analyses described in this analysis plan have been conducted by the authors making this a retrospective registration.

### Explanation of foreknowledge and managing unintended influences

This is a retrospective registration. The analysis was conducted and published prior to this OSF registration. The manuscript is available at Zenodo (DOI: 10.5281/zenodo.23884236) and Figshare (DOI: 10.6084/m9.figshare.34884417), and the Python package is available on PyPI (mws-lab).

To mitigate risks of unintended influences on the analysis plan and conclusions, the following steps were taken:

1. Data provenance is fully documented: all five indicators are extracted from the World Bank WDI API via a public, reproducible script (mws_lab/fetch.py). The national indicators are sourced from Morocco's 2025 State of the Environment Report.

2. No imputation or interpolation: missing values are kept missing, and the complete-case window (2004–2019, n = 16) is determined entirely by the data availability of the irrigated-land and withdrawals series.

3. Model specification is fixed ex ante: FW_t = β0 + β1·IRRIG_t + β2·POPGR_t + β3·YIELD_t + β4·ARABLE_t + ε_t. No predictor was added or removed after observing results.

4. Diagnostics are reported in full, not selectively: R², adjusted R², RMSE, MAE, MAPE, coefficient standard errors, 95% CIs, VIFs, and the design-matrix condition number κ(X) ≈ 78,500 are all reported, including the severe multicollinearity finding.

5. All results are framed as associational: no hypothesis test is treated as confirmatory, and no causal claim is made.

6. The analysis is reproducible from the public data and the published Python package (mws-lab on PyPI).

The purpose of this registration is to document the analysis plan transparently, not to claim a pre-registered confirmatory design.

---

## Research Design

### Study type

Non-randomized study: Does not include random assignment of subjects to treatments or conditions. This usually includes correlational studies, observational studies, surveys, natural experiments, real-world evidence studies, regression discontinuity designs, and descriptive studies.

### Intention for causal interpretation

No causal relationship inferred: This study is not intended to inform a causal relationship.

### Blinding of experimental treatments

No blinding is involved.

### Additional blinding during research or analysis

Not applicable. This is an observational analysis of publicly available data. No experimental treatments or blinding procedures are involved. The analysis plan is documented transparently in the published manuscript.

### Study design

Observational, associational time-series analysis of Morocco's national freshwater withdrawals (2000–2025).

Design parameters:
- Unit of analysis: country-year (Morocco, annual observations).
- Panel window: 2000–2025 (data availability varies by indicator).
- Model estimation window: 2004–2019 (complete-case, n = 16). This window is determined entirely by data availability: the irrigated-land series begins in 2004, and the withdrawals series is available through 2022.
- Design type: between-unit (unpaired) observational panel. No within-unit manipulation, no counterbalancing, no randomization.
- Variables: 1 target (annual freshwater withdrawals, FW) and 4 predictors (irrigated land share, IRRIG; population growth rate, POPGR; cereal yield, YIELD; arable land share, ARABLE).
- Estimation: Ordinary Least Squares (OLS) on the complete-case window.
- Diagnostics: R², adjusted R², RMSE, MAE, MAPE, coefficient standard errors, 95% confidence intervals, VIFs, design-matrix condition number κ(X), pairwise Pearson correlations on pairwise-complete observations.

The design does not support causal identification. All results are reported as associations. Climate variables (rainfall, temperature, evapotranspiration) are discussed qualitatively but are not included as regressors, due to the limited sample size and the priority of preserving the OLS degrees of freedom.

**Attached:** `water_scarcity_morocco.pdf`, `README.md`

### Randomization

Not applicable. This is an observational study with no randomization procedure. The panel is defined by the complete set of available annual observations for Morocco over the specified window.

---

## Sampling

### Data collection procedures

This study uses secondary data. No new data are collected. All data are obtained from two public sources:

(1) World Bank World Development Indicators (WDI), annual series for Morocco (2000–2025). Retrieved via the World Bank public API (https://api.worldbank.org/v2/country/MA/indicator/{indicator}) using a reproducible Python script (mws_lab/fetch.py, published on PyPI as mws-lab). Five indicators are used:
- ER.H2O.FWTL.K3 — Annual freshwater withdrawals (billion m³)
- AG.LND.IRIG.AG.ZS — Agricultural land irrigated (% of agricultural land)
- SP.POP.GROW — Population growth (annual %)
- AG.YLD.CREL.KG — Cereal yield (kg per hectare)
- AG.LND.ARBL.ZS — Arable land (% of land area)

(2) Morocco State of the Environment Report 2025 (national indicators): renewable water resources per capita, potential and mobilizable water resources, groundwater abstraction, sectoral water allocation, seasonal rainfall, and national dam-filling rates for 2025–2026.

Population: Morocco, annual observations, 2000–2025.
Sampling frame: all available annual observations for Morocco in the World Bank WDI and the 2025 State of the Environment Report.
Inclusion criteria: annual observations for Morocco for the five specified indicators within 2000–2025.
Exclusion criteria: observations missing for any of the five indicators in a given year are excluded from the complete-case multivariate model. No imputation or interpolation is applied.
Geographic scope: Morocco (national level).
Expected duration of data collection: instantaneous (script execution, <1 minute). The data are static once retrieved.

### Sample size

Unit of analysis: country-year (Morocco, annual).

Model sample: n = 16 (complete-case window 2004–2019). This is the intersection of:
- Irrigated-land series availability (starts 2004)
- Withdrawals series availability (ends 2022)
- Complete data on all five indicators

Pairwise-complete samples vary by pair:
- Withdrawals ↔ Irrigated land: n = 16
- Withdrawals ↔ Cereal yield: n = 23
- Withdrawals ↔ Population growth: n = 23
- Withdrawals ↔ Arable land: n = 23
- Irrigated land ↔ Population growth: n = 16
- Population growth ↔ Arable land: n = 25
- Irrigated land ↔ Arable land: n = 16

No conditions, treatments, or clusters are involved (observational design). The sample size is determined entirely by data availability.

### Sample size rationale

No power analysis was performed. The sample size (n = 16) is determined entirely by data availability: the irrigated-land series begins in 2004, and the withdrawals series ends in 2022. The complete-case window (2004–2019) is the intersection of these two constraints.

Because the sample size is small, the analysis is explicitly framed as exploratory. Individual coefficient estimates are not treated as confirmatory, and the severe multicollinearity (κ(X) ≈ 78,500) is reported as a finding rather than corrected. All reported quantities (R², CIs, condition number) are presented with the small-sample caveat explicit in the manuscript.

### Starting and stopping rules

Starting rule: data collection is a single API call to the World Bank WDI endpoint, executed by mws_lab/fetch.py. There is no pilot phase and no sequential data collection. The data are retrieved once and used as-is.

Stopping rule: no stopping rule is needed because the data are static and publicly available. All available annual observations for the five indicators (2000–2025) are retrieved. The complete-case window (2004–2019) is determined mechanically by the intersection of the two limiting series, not by any decision on the part of the analyst.

No interim analyses, no sequential testing, no stopping for futility or success.

---

## Variables

### Manipulated variables

None. This is an observational study with no manipulated variables, no treatment arms, and no randomization.

### Measured variables

Outcome (target variable):
- FW_t — Annual freshwater withdrawals in Morocco, billion m³ (World Bank: ER.H2O.FWTL.K3). Available 2000–2022.

Predictors (observational, not manipulated):
- IRRIG_t — Agricultural land irrigated, % of agricultural land (World Bank: AG.LND.IRIG.AG.ZS). Available 2004–2019.
- POPGR_t — Population growth, annual % (World Bank: SP.POP.GROW). Available 2000–2025.
- YIELD_t — Cereal yield, kg per hectare (World Bank: AG.YLD.CREL.KG). Available 2000–2024.
- ARABLE_t — Arable land, % of land area (World Bank: AG.LND.ARBL.ZS). Available 2000–2024.

Descriptive variables (used in the water-balance discussion, not in the OLS model):
- Renewable water resources per capita (m³/person/year), 2025 (≈600).
- Potential natural water resources (billion m³/year, ≈22).
- Technically mobilizable resources (billion m³/year, ≈8).
- Groundwater abstraction (billion m³/year, ≈5).
- Water-stress index (%, 2022, 50.75%).
- Sectoral allocation shares (%): agriculture ≈88, drinking water ≈11, industry/tourism ≈1.
- Seasonal rainfall (mm): 2015–2020 average 307.9; 2024–2025 = 293; 2025–2026 = 462.
- National dam-filling rate (%): 31 Oct 2025 = 31.29; 31 Oct 2026 = 65.81.

Derived variables used in the model:
- Time index t (year), included implicitly through the time-series structure.

No covariates beyond the four listed predictors are included in the OLS model. No variable is used for subsetting beyond the complete-case rule (all five indicators must be non-missing in a given year).

### Indices

Three derived indicators are defined in the manuscript (Supplementary Indicators). None of them enters the OLS regression; they are used only in the descriptive discussion.

Per-capita renewable water (PCW):
PCW_t = RWR_t / POP_t
where RWR_t is renewable water resources and POP_t is total population. Units: m³/person/year.

Water-stress index (WSI):
WSI_t = (Total withdrawals_t / RWR_t) × 100%
Units: percent.

Dam-filling rate (DFR):
DFR_t = (Stored reservoir volume_t / Total reservoir capacity) × 100%
Units: percent.

No composite index, no factor score, no weighted sum is constructed. The four predictors in the OLS model are used in their raw published form (World Bank WDI definitions), not transformed. No principal component analysis, no standardization beyond what OLS inherently performs, no aggregation of indicators into a single latent variable.

---

## Analysis Plan

### Statistical models

The primary statistical model is an Ordinary Least Squares (OLS) multiple regression, specified as:

FW_t = β0 + β1·IRRIG_t + β2·POPGR_t + β3·YIELD_t + β4·ARABLE_t + ε_t

where:
- FW_t = annual freshwater withdrawals (billion m³) in year t
- IRRIG_t = irrigated share of agricultural land (%)
- POPGR_t = population growth rate (annual %)
- YIELD_t = cereal yield (kg/ha)
- ARABLE_t = arable land share (%)
- ε_t = error term

Estimation: OLS via matrix algebra, β̂ = (XᵀX)⁻¹Xᵀy, on the complete-case window 2004–2019 (n = 16).

Model fit and diagnostics reported:
- R² and adjusted R² [1 − (1−R²)(n−1)/(n−k−1)]
- RMSE, MAE, MAPE
- Coefficient standard errors, t-statistics, 95% confidence intervals
- Variance Inflation Factors: VIF_j = 1/(1−R²_j)
- Design-matrix condition number: κ(X) = σ_max/σ_min
- Pairwise Pearson correlations on pairwise-complete observations, with n recorded per pair

No interactions, no subgroup analyses, no pairwise contrasts, no follow-up tests are specified. No positive or negative controls are used (observational design). No convergence criteria (closed-form OLS, not iterative). Assumption checks are reported as findings, not used as gates: severe multicollinearity (κ(X) ≈ 78,500) is reported explicitly, and individual coefficient magnitudes are not interpreted as independent effects.

Secondary analyses:
- Pairwise Pearson correlations (reported with n per pair).
- Descriptive water-balance calculations from the 2025 State of the Environment Report (per-capita water, water-stress index, sectoral shares, dam-filling rate).

### Transformations

No transformations are applied. All variables enter the OLS model in their raw published form (World Bank WDI definitions).

- No centering, no scaling, no standardization beyond what OLS performs inherently.
- No logging, no differencing, no detrending.
- No winsorizing, no trimming, no outlier removal.
- No coding of categorical variables (all predictors are continuous).
- No recoding, no collapsing, no binning.

The time index (year) is not included as a separate regressor; the model is a static OLS on the levels of the five variables over the complete-case window.

### Inference criteria

The analysis is exploratory and associational. Inference is descriptive, not confirmatory.

Reported quantities:
- R² = 0.812 and adjusted R² = 0.744 (goodness of fit)
- Coefficient estimates with standard errors and 95% confidence intervals
- Condition number κ(X) ≈ 78,500 (multicollinearity diagnostic)
- VIFs per predictor
- Pairwise Pearson r with n per pair

No p-value thresholds are used to declare "significance." No one-tailed or two-tailed tests are treated as confirmatory. Where 95% CIs are reported (as in the manuscript), they are presented descriptively: for the irrigated-land coefficient, the CI excludes zero; for the arable-land coefficient, the CI is near but not clearly excluding zero; for population growth, the CI is wide; for cereal yield, the CI is narrow and centered near zero.

Multiple comparisons: because no hypothesis tests are treated as confirmatory, no correction (Bonferroni, Holm, FDR) is applied. The framing is hypothesis-generating.

Model fit interpretation: κ(X) ≈ 78,500 indicates severe multicollinearity, and individual coefficient magnitudes are reported as unstable. No coefficient is interpreted as an independent causal effect. The model's joint explanatory power (R²) is reported as a description of the shared variance among the five series.

### Data inclusion and exclusion

Inclusion criteria:
- Country: Morocco (World Bank country code MA).
- Years: 2000–2025 (data availability varies by indicator).
- Indicators: ER.H2O.FWTL.K3, AG.LND.IRIG.AG.ZS, SP.POP.GROW, AG.YLD.CREL.KG, AG.LND.ARBL.ZS.
- Complete-case rule for the OLS model: a year enters the regression only if all five indicators are non-missing in that year. This yields 2004–2019 (n = 16).

Exclusion criteria:
- Years with any missing indicator are excluded from the OLS model (not from the pairwise-complete correlations, which use their own pairwise n).
- No observations are excluded for being outliers. No trimming, no winsorizing, no influence diagnostics are used to remove observations.

Pairwise correlations use pairwise-complete observations, and n is reported for each pair (ranging from 16 to 25).

No subjects (human participants) are involved. No exclusions based on demographic, geographic, or behavioral criteria.

### Missing data

Missing data are not imputed and not interpolated.

- The complete-case window for the OLS model is 2004–2019 (n = 16), determined mechanically by the intersection of available series (irrigated land starts 2004; withdrawals ends 2022).
- Pairwise correlations use pairwise-complete observations: n is recorded per pair (ranging 16–25).
- No multiple imputation, no maximum likelihood, no EM algorithm, no last-observation-carried-forward, no mean substitution.
- The manuscript explicitly states: "No missing values were imputed or interpolated."

The consequence of this choice is that the OLS sample is small (n = 16), and this limitation is reported prominently in the manuscript and on the project website.

### Other planned analysis

Secondary and descriptive analyses (reported but not central to the associational claim):

1. National water balance (from Morocco 2025 State of the Environment Report):
   - Renewable water per capita (2025) ≈ 600 m³/person/year
   - Potential natural water resources ≈ 22 billion m³/year
   - Technically mobilizable resources ≈ 8 billion m³/year
   - Groundwater abstraction ≈ 5 billion m³/year
   - Water-stress index (2022) = 50.75%

2. Sectoral allocation shares:
   - Agriculture ≈ 88%
   - Drinking water ≈ 11%
   - Industry/tourism ≈ 1%

3. Rainfall and dam-filling observations (2015–2026):
   - Average seasonal rainfall 2015–2020: 307.9 mm
   - 2024–2025 season: 293 mm
   - 2025–2026 season: 462 mm
   - National dam-filling rate 31 Oct 2025: 31.29%
   - National dam-filling rate 31 Oct 2026: 65.81%

4. Per-capita decline narrative (1960–2020): from ≈2,560 m³/year to ≈620 m³/year.

5. Policy implications (discussion section): irrigation efficiency, per-capita and per-basin monitoring, better data.

No sensitivity analyses across alternative specifications, no robustness checks with different windows, no alternative estimators (e.g., robust standard errors, ridge regression) are performed. These are stated as future work in the manuscript.

The analysis is reproducible from the public data and the published Python package (mws-lab on PyPI). The full manuscript is available at Zenodo (10.5281/zenodo.23884236) and Figshare (10.6084/m9.figshare.34884417).

---

## Other

### Context and additional information

CONTEXT

This is a retrospective registration. The manuscript, figures, data, and Python package were all published prior to this OSF registration. The purpose of this registration is to document the analysis plan transparently and to provide a permanent, citable record alongside the Zenodo, Figshare, and PyPI deposits.

PUBLISHED RESOURCES

- Zenodo DOI (manuscript): 10.5281/zenodo.23884236
- Figshare DOI (figures): 10.6084/m9.figshare.34884417
- PyPI package: mws-lab — https://pypi.org/project/mws-lab/
- Project website: https://mws-lab.netlify.app
- ORCID: https://orcid.org/0009-0003-8903-0029

The Python package (mws-lab) includes the reproducible data-fetch script (mws_lab/fetch.py) and the World Bank WDI extract (mws_lab/data/worldbank_data.csv). Installing the package and running the fetch script reproduces the raw dataset. The full analysis pipeline (descriptive statistics, pairwise correlations, OLS with diagnostics) is documented in the manuscript.

INTERPRETIVE FRAMING

The analysis is exploratory and associational. The manuscript states explicitly: "It is not designed to establish causal attribution, and its conclusions should be read as hypothesis-generating rather than confirmatory."

The severe multicollinearity (κ(X) ≈ 78,500) is reported as a finding, not corrected. Individual coefficient magnitudes and signs are unstable and must not be read as independent causal effects.

SCOPE AND NON-GOALS

- No causal identification (no quasi-experimental design, no instrumental variables).
- No basin-level disaggregation (national indicators only).
- No direct climate variables in the regression (rainfall, temperature, evapotranspiration are discussed qualitatively).
- No sub-annual or seasonal analysis.
- No cross-country generalization.

These are stated as future research directions in the manuscript (basin-level panels, direct climate variables, causal identification strategies, infrastructure effects, behavioral mediation).

DATA SOURCES

- World Bank World Development Indicators (WDI), public domain (CC-BY-4.0): https://datacatalog.worldbank.org/public-licenses
- Morocco State of the Environment Report 2025 (national indicators).

LICENSING

- Code: MIT License
- Manuscript, figures, documentation: CC-BY-4.0
- Data: World Bank CC-BY-4.0

ACKNOWLEDGMENTS

This is an independent research project. No institutional funding, no external funding. The work was conducted at the Ronin Institute / Rite of Renaissance.

REPRODUCIBILITY

The full analysis is reproducible:
1. pip install mws-lab
2. python -c "from mws_lab import fetch; fetch.main()"
3. Follow the methodology in the manuscript (Zenodo DOI above) to reproduce R² = 0.812, n = 16, κ(X) ≈ 78,500.

The complete manuscript is attached as a PDF to this registration.

---

## Metadata

### Contributors
Samir Baladi

### Resource type
No resource type

### Description

An exploratory associational analysis of the climatic, agricultural, and socioeconomic drivers of national freshwater withdrawals in Morocco (2000–2025). The study uses five publicly available World Bank WDI indicators, supplemented by national indicators from Morocco's 2025 State of the Environment Report, and applies ordinary least squares regression with full diagnostics (VIF, condition number, confidence intervals).

Key results: R² = 0.812 (adjusted 0.744) on a complete-case sample of n = 16 (2004–2019), with a design-matrix condition number of κ(X) ≈ 78,500 indicating severe multicollinearity. Agriculture absorbs ≈88% of total water allocation. Morocco's renewable freshwater per capita fell from roughly 2,560 m³/year in 1960 to about 620 m³ in 2020.

The analysis is explicitly exploratory and associational. It is not designed to establish causal attribution, and its conclusions should be read as hypothesis-generating rather than confirmatory.

Resources:
- Zenodo DOI: 10.5281/zenodo.23884236
- Figshare DOI: 10.6084/m9.figshare.34884417
- PyPI: https://pypi.org/project/mws-lab/
- Website: https://mws-lab.netlify.app

License: MIT (code) + CC-BY-4.0 (manuscript, figures, documentation).

Author: Samir Baladi (ORCID: 0009-0003-8903-0029)

### Registration Type
OSF Preregistration

### Registry
OSF Registries

### Associated project
https://osf.io/6m9ef

### Date Created
Nov 3, 2026, 4:04 AM

### Date registered
Nov 3, 2026, 4:04 AM

### Subjects
- Water Resource Management
- Earth Sciences
- Environmental Sciences
- Physical Sciences and Mathematics

### Tags
- agricultural water demand
- climate variability
- environmental science
- freshwater withdrawals
- irrigation efficiency
- OLS regression
- water morocco scarcity
- water policy
- World Bank indicators

### Affiliated Institutions
No affiliated institutions

### Funder Names
No information

### Language
No language

### Associated project
https://osf.io/6m9ef

### Internet Archive link
(Pending)

### License
CC-By Attribution 4.0 International

### Registration DOI
No DOI (Pending)

---

## Citations

### APA
Baladi, S. (2026, November 3). mws-lab — Water Scarcity in Morocco: A Multivariate Analysis of Climatic, Agricultural, and Socioeconomic Drivers. OSF. (DOI pending)

### MLA
Baladi, Samir. "mws-lab — Water Scarcity in Morocco: A Multivariate Analysis of Climatic, Agricultural, and Socioeconomic Drivers." OSF, 3 Nov. 2026. Web.

### Chicago
Baladi, Samir. 2026. "mws-lab — Water Scarcity in Morocco: A Multivariate Analysis of Climatic, Agricultural, and Socioeconomic Drivers." OSF. November 3.

### BibTeX

```bibtex
@misc{baladi2026mws_osf,
  author       = {Baladi, Samir},
  title        = {{mws-lab} --- Water Scarcity in {Morocco}:
                  A Multivariate Analysis of Climatic, Agricultural,
                  and Socioeconomic Drivers},
  year         = {2026},
  month        = nov,
  day          = {3},
  publisher    = {OSF},
  note         = {OSF Preregistration (DOI pending)}
}
```

---

Source: Center for Open Science · OSF Registries
Retrieved: 2026-11-03

