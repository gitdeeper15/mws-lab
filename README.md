<div align="center">

# Water Scarcity in Morocco

### A Multivariate Analysis of Climatic, Agricultural, and Socioeconomic Drivers

*Exploratory Associational Analysis · World Bank Indicators 2000–2025 · OLS Diagnostics · Policy Implications*

---

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23884236-1B4F72?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.23884236)
[![PyPI](https://img.shields.io/badge/PyPI-mws--lab-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/mws-lab/)
[![Figshare](https://img.shields.io/badge/Figshare-10.6084%2Fm9.figshare.34884417-FC4B00?logo=figshare&logoColor=white)](https://doi.org/10.6084/m9.figshare.34884417)
[![Website](https://img.shields.io/badge/website-mws--lab.netlify.app-00C7B7?logo=netlify&logoColor=white)](https://mws-lab.netlify.app)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0003-8903-0029)
[![Domain](https://img.shields.io/badge/domain-Earth%20%26%20Environmental%20Sciences-2e8b57)]()
[![Data](https://img.shields.io/badge/data-World%20Bank%20WDI-1B4F72)](https://data.worldbank.org/country/morocco)
[![Python](https://img.shields.io/badge/analysis-Python-3776ab?logo=python&logoColor=white)](https://python.org)
[![Status](https://img.shields.io/badge/status-exploratory--associational-blue)]()
[![Causal](https://img.shields.io/badge/causal%20claims-none-orange)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-27ae60)](LICENSE)

---

**`5 WDI Indicators`** · **`2000–2025 Panel`** · **`n = 16 Model Sample`** · **`R² = 0.812`** · **`κ ≈ 78,500`** · **`88% Agricultural Share`**

---

[Research Paper](PUBLICATION/water_scarcity_morocco.pdf) · [Key Findings](#-key-findings) · [Methodology](#-methodology) · [Results](#-results) · [Limitations](#-limitations) · [Policy Implications](#-policy-implications) · [Citation](#-citation)

</div>

---

## 📌 Overview

Morocco's renewable freshwater per capita fell from roughly **2,560 m³ per year in 1960** to about **620 m³ in 2020**, well inside the United Nations' absolute water-scarcity threshold. Internal renewable water resources stood at **777 m³ per capita in 2022**, and the national water-stress index reached **50.75%** that year.

This study asks how three classes of drivers (climatic, agricultural, and socioeconomic) relate to the trajectory of **national freshwater withdrawals** between 2000 and 2025. It uses five publicly available World Bank indicators, supplemented by national indicators from Morocco's 2025 State of the Environment Report.

> The analysis is **exploratory and associational**. It is not designed to establish causal attribution, and its conclusions should be read as **hypothesis-generating rather than confirmatory**.

### Research Question

What are the relative contributions of agricultural land-use change, agricultural productivity, and population growth to the observed pattern of freshwater withdrawals in Morocco, and what do the strength and structure of these associations imply for water policy?

---

## 🗂️ Table of Contents

- [Overview](#-overview)
- [Key Findings](#-key-findings)
- [Conceptual Framework](#-conceptual-framework)
- [Data Sources](#-data-sources)
- [Methodology](#-methodology)
- [Results](#-results)
- [Discussion Highlights](#-discussion-highlights)
- [Policy Implications](#-policy-implications)
- [Limitations](#-limitations)
- [Future Research](#-future-research)
- [Repository Structure](#-repository-structure)
- [Reproducing the Analysis](#-reproducing-the-analysis)
- [Research Paper](#-research-paper)
- [Platforms](#-platforms)
- [Citation](#-citation)
- [Key References](#-key-references)
- [License](#-license)
- [Author](#-author)

---

## 🔑 Key Findings

| # | Finding |
|---|---------|
| 1 | Per-capita renewable water fell by roughly three-quarters between 1960 and 2020 (≈2,560 → ≈620 m³/yr). |
| 2 | Agriculture absorbs about **88%** of total water allocation, against 11% for drinking water and 1% for industry and tourism. |
| 3 | National freshwater withdrawals fell from **12.60** to **10.573 billion m³** (2000 → 2010) and were reported at that level through 2022, even as cereal yield rose from 366.8 to 1,240.1 kg/ha. |
| 4 | An exploratory OLS model (2004–2019, n = 16) reaches **R² = 0.812** (adjusted 0.744), but the design matrix condition number of about **78,500** signals severe multicollinearity. |
| 5 | Irrigated land and population growth are strongly inversely correlated (**r = −0.89**), so their effects cannot be separated in this dataset. |
| 6 | The 2025–2026 rainfall and dam-filling rebound is a short-term storage buffer, **not** a reversal of the long-run per-capita decline. |

---

## 🧭 Conceptual Framework

```
CLIMATE DRIVERS ──→ HYDROLOGICAL SYSTEM ──→ WATER AVAILABILITY
 Rainfall               Runoff                 Renewable supply
 Temperature            Reservoirs             Per-capita water
 Drought                Aquifers                     │
                             │                       │
                             ↓                       ↓
                  SOCIOECONOMIC PRESSURES     SECTORAL DEMAND
                  Population · Urban demand   Agriculture · Drinking
                                              water · Industry
                             │                       │
                             └───────────┬───────────┘
                                         ↓
                              WATER SECURITY OUTCOMES
                              Scarcity · Allocation · Resilience
```

The framework is adapted from the structural relationships described in the reviewed literature. Climate variables enter the discussion qualitatively; they are **not** regressors in the model.

---

## 📥 Data Sources

### 1. World Bank World Development Indicators (annual, Morocco, 2000–2025)

| Variable | Indicator Code | Notes |
|----------|----------------|-------|
| Arable land (% of land area) | `AG.LND.ARBL.ZS` | 19.64% (2000) → 15.84% (2024) |
| Agricultural land irrigated (% of agricultural land) | `AG.LND.IRIG.AG.ZS` | Reported from 2004; 4.30% (2004) → 5.96% (2019) |
| Cereal yield (kg per hectare) | `AG.YLD.CREL.KG` | 366.8 (2000) → 1,240.1 (2024) |
| Annual freshwater withdrawals (billion m³) | `ER.H2O.FWTL.K3` | Reported through 2022 |
| Population growth (annual %) | `SP.POP.GROW` | 1.40% (2000) → 0.91% (2025) |

### 2. Morocco State of the Environment Report 2025

Renewable water resources per capita, potential and mobilizable water resources, groundwater abstraction, sectoral water allocation, seasonal rainfall, and national dam-filling rates for 2025 and 2026.

The two sources are kept analytically distinct. The World Bank panel supports the multivariate analysis; the national indicators support the descriptive water-balance and recovery discussion. **No missing values were imputed or interpolated.**

---

## 🔬 Methodology

### Analytical Workflow

```
┌────────────────────────────────────────────────────────────┐
│  1. Data Acquisition     →  Government reports · World Bank│
│  2. Data Harmonization   →  Units · periods · metadata     │
│  3. Quality Control      →  Missingness · outliers · source│
│  4. Exploratory Analysis →  Descriptives · trends          │
│  5. Empirical Modelling  →  Correlation · OLS (validated)  │
│  6. Robustness Checks    →  Diagnostics · specifications   │
│  7. Interpretation       →  Policy implications · limits   │
└────────────────────────────────────────────────────────────┘
```

### Regression Specification

```
FW_t = β0 + β1·IRRIG_t + β2·POPGR_t + β3·YIELD_t + β4·ARABLE_t + ε_t

β̂ = (XᵀX)⁻¹ Xᵀy
```

| Symbol | Variable |
|--------|----------|
| `FW` | Annual freshwater withdrawals |
| `IRRIG` | Irrigated share of agricultural land |
| `POPGR` | Population growth rate |
| `YIELD` | Cereal yield |
| `ARABLE` | Arable land share |

Because irrigated land is reported only from 2004 and withdrawals only through 2022, the **complete-case sample is 2004–2019 (n = 16)**.

### Metrics and Diagnostics

| Purpose | Measure |
|---------|---------|
| Model fit | R², adjusted R² = 1 − (1 − R²)(n − 1)/(n − k − 1) |
| Predictive error | RMSE, MAE, MAPE |
| Bivariate association | Pearson r on pairwise-complete observations |
| Coefficient uncertainty | Standard error, t-statistic, 95% confidence interval |
| Multicollinearity | VIF_j = 1/(1 − R²_j), condition number κ(X) = σ_max/σ_min |

A condition number above about 30 is conventionally taken to indicate moderate-to-severe multicollinearity.

### Supplementary Indicators

```
PCW_t = RWR_t / POP_t                              (per-capita renewable water)
WSI_t = (Total withdrawals_t / RWR_t) × 100%       (water-stress index)
DFR_t = (Stored reservoir volume_t / Total reservoir capacity) × 100%   (dam-filling rate)
```

---

## 📊 Results

### National Water Balance (State of the Environment Report 2025)

| Indicator | Value |
|-----------|-------|
| Renewable water per capita (2025) | ≈ 600 m³/person/year |
| Potential natural water resources | ≈ 22 billion m³/year |
| Technically mobilizable resources | ≈ 8 billion m³/year |
| Groundwater abstraction | ≈ 5 billion m³/year |
| Water-stress index (2022) | 50.75% |

Only a minority of the nominal resource base is operationally accessible.

### Sectoral Allocation

| Sector | Share |
|--------|-------|
| Agriculture | ≈ 88% |
| Drinking water | ≈ 11% |
| Industry and tourism | ≈ 1% |

This is consistent with the historical 75–87% range reported for irrigation's share of national withdrawals.

### Rainfall and Dam-Filling Recovery

| Observation | Value |
|-------------|-------|
| Average seasonal rainfall, 2015–2020 | 307.9 mm |
| Season 2024–2025 | 293 mm |
| Season 2025–2026 | 462 mm |
| National dam-filling rate, 31 Oct 2025 | 31.29% |
| National dam-filling rate, 31 Oct 2026 | 65.81% |

The observations do not form a continuous annual series and are plotted on separate axes.

### Pairwise Correlations (pairwise-complete)

| Pair | r | n |
|------|---|---|
| Withdrawals ↔ Irrigated land | −0.70 | 16 |
| Withdrawals ↔ Cereal yield | −0.36 | 23 |
| Withdrawals ↔ Population growth | 0.49 | 23 |
| Withdrawals ↔ Arable land | 0.67 | 23 |
| **Irrigated land ↔ Population growth** | **−0.89** | 16 |
| Population growth ↔ Arable land | 0.78 | 25 |
| Irrigated land ↔ Arable land | −0.44 | 16 |

### Exploratory OLS Model (2004–2019, n = 16)

| Statistic | Value |
|-----------|-------|
| R² | 0.812 |
| Adjusted R² | 0.744 |
| Condition number κ(X) | ≈ 78,500 |

| Predictor | Approximate coefficient | Reading |
|-----------|-------------------------|---------|
| Irrigated land | ≈ −3 | Negative, relatively tightly estimated; 95% CI excludes zero |
| Population growth | ≈ −14 | Largest magnitude, wide interval; strongly collinear with irrigated land |
| Cereal yield | ≈ 0 | Close to zero, narrow interval |
| Arable land | small positive | Interval close to, but not clearly excluding, zero |

With a condition number in the tens of thousands, individual coefficient magnitudes and signs are unstable and **must not be read as independent causal effects**. The model is reported as a description of joint explanatory power only.

---

## 💬 Discussion Highlights

- **Total withdrawals versus per-capita scarcity.** Population growth drives long-run per-capita scarcity through the denominator of the per-capita ratio, while agricultural demand is the proximate lever on total withdrawals. A policy that stabilizes withdrawals while population grows will still see per-capita water security erode.
- **Multicollinearity as a finding.** Irrigation expansion, cereal productivity growth, and demographic deceleration moved together as a largely non-separable complex. Separating them needs longer series, basin-level panels, or quasi-experimental variation.
- **Interpretive risk of a wet year.** A single favorable season can overshadow a multi-decade structural decline. Reservoir storage is a short-horizon buffer; per-capita availability is a slow-moving structural indicator.
- **Efficiency signal.** Withdrawals were broadly stable to declining after 2010 while cereal yield rose substantially, which is consistent with efficiency gains and adaptive farmer behavior reported in the literature.

---

## 🧩 Policy Implications

1. **Irrigation efficiency.** Because agriculture accounts for about 88% of allocation, drip and precision irrigation, crop-water-productivity-oriented extension services, and support for less water-intensive crop portfolios in the most stressed basins are the largest single lever.
2. **Per-capita and per-basin monitoring.** Water-security planning should be expressed in per-capita and per-basin terms, not only in aggregate withdrawals or dam storage, to avoid over-reading favorable rainfall years.
3. **Better data.** Basin-level and sub-annual data on groundwater abstraction, aquifer depletion, and disaggregated sectoral consumption would allow agricultural, climatic, and demographic effects to be separated with greater statistical independence.

---

## ⚠️ Limitations

| Type | Concern |
|------|---------|
| Sample size | Only n = 16 for the multivariate model, limited by the irrigated-land series |
| Multicollinearity | κ(X) ≈ 78,500; coefficients are unstable and not independently interpretable |
| Missing climate variables | No rainfall, temperature, or evapotranspiration in the regression; climate is discussed qualitatively |
| Aggregation | National indicators mask heterogeneity across river basins |
| Inference | All relationships are associational; no hypothesis test is treated as confirmatory |
| Indicator coverage | Withdrawals are reported only through 2022; some series are partially incomplete |

---

## 🔭 Future Research

| Direction | Focus |
|-----------|-------|
| Basin-level panels | Disaggregate by river basin to capture aridity, irrigation intensity, groundwater depletion |
| Direct climate variables | Add rainfall, temperature, and evapotranspiration to the model |
| Causal identification | Quasi-experimental or instrumental-variable methods (for example staggered irrigation scheme rollouts) |
| Infrastructure effects | Reservoir sedimentation and effective storage capacity |
| Behavioral and technological mediation | Irrigation technology adoption and farmer adaptation |

---

## 📁 Repository Structure


```
mws-lab/
├── README.md
├── AUTHORS.md
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE
├── MANIFEST.in
├── VERSION
├── pyproject.toml
├── requirements.txt
├── setup.py
├── setup.cfg
├── upload_morocco.py
│
├── morocco_water_scarcity/          # Python package (pending build)
│   ├── __init__.py
│   ├── fetch.py
│   └── data/
│       ├── worldbank_data.csv
│       └── input.json
│
├── DATA/
│   └── raw/
│       ├── fetch_worldbank_data.py
│       ├── worldbank_data.csv
│       └── input.json
│
├── ANALYSIS/
│   ├── ANALYSIS_REPORT.md
│   └── analysis_insights.json
│
├── PUBLICATION/
│   ├── water_scarcity_morocco.pdf   # Manuscript
│   ├── figures/                     # 7 figures
│   ├── Netlify/                     # Website source
│   ├── dist/                        # (to be rebuilt)
│   ├── credit_table.md
│   ├── manifest.json
│   └── netlify.toml
│
├── REPORTS/                         # Governance and audit
├── EXTERNAL_REVIEW/
├── VALIDATION/
└── docs/
    ├── ITERATION_LOG.md
    └── comprehensive_audit_report.json
```

---

## ♻️ Reproducing the Analysis

The paper reports that all computation was performed in **Python** with standard numerical and statistical libraries. To reproduce it:

1. Download the five World Bank indicators listed in [Data Sources](#-data-sources) for Morocco, 2000–2025.
2. Keep missing values missing; do not impute or interpolate.
3. Compute Pearson correlations on pairwise-complete observations and record n for each pair.
4. Restrict the regression to the complete-case window **2004–2019 (n = 16)**.
5. Estimate Equation 1 by OLS and report R², adjusted R², RMSE, MAE, MAPE, coefficient standard errors, 95% CIs, VIFs, and the design-matrix condition number.
6. Treat every result as associational.

---

## 📄 Research Paper

**Title:** Water Scarcity in Morocco: A Multivariate Analysis of Climatic, Agricultural, and Socioeconomic Drivers

**Status:** Initial Research Manuscript — Exploratory Multivariate Analysis
**Domain:** Earth and Environmental Sciences — Environmental Management, Policy and Planning
**Version:** 1.0 · November 2026
**DOI:** [10.5281/zenodo.23884236](https://doi.org/10.5281/zenodo.23884236)

See [`PUBLICATION/water_scarcity_morocco.pdf`](PUBLICATION/water_scarcity_morocco.pdf) for the full manuscript.

**Keywords:** Water scarcity · Morocco · Water stress · Irrigation · Freshwater withdrawals · Climate variability · Agricultural water demand · Population growth · Multivariate analysis · Water policy

---

## 🌐 Platforms

| Platform | URL | Role |
|----------|-----|------|
| Zenodo | [doi.org/10.5281/zenodo.23884236](https://doi.org/10.5281/zenodo.23884236) | Citable DOI, manuscript archive |
| ORCID | [orcid.org/0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) | Researcher identity |
| World Bank Data | [data.worldbank.org/country/morocco](https://data.worldbank.org/country/morocco) | Source of the five WDI indicators |

---

## 📖 Citation

If this work contributes to your research, please cite it as follows.

### BibTeX

```bibtex
@article{baladi2026waterscarcity,
  author       = {Baladi, Samir},
  title        = {Water Scarcity in {Morocco}: A Multivariate Analysis of
                  Climatic, Agricultural, and Socioeconomic Drivers},
  year         = {2026},
  month        = nov,
  version      = {1.0},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23884236},
  url          = {https://doi.org/10.5281/zenodo.23884236},
  note         = {Ronin Institute / Rite of Renaissance. Exploratory associational analysis}
}
```

### APA

> Baladi, S. (2026). *Water scarcity in Morocco: A multivariate analysis of climatic, agricultural, and socioeconomic drivers* (Version 1.0). Zenodo. https://doi.org/10.5281/zenodo.23884236

---

## 📚 Key References

1. Boudhar, S., & Boudhar, A. (2025). Water scarcity and the agricultural trade structure in Morocco: A quantification of virtual water flows in Morocco's foreign trade of agricultural products. https://doi.org/10.21203/rs.3.rs-6080363/v1
2. Sana, A., Chfadi, T., & El Mansoum, R. (2026). From belief to behavior: An exploratory analysis of adaptive behavior to water scarcity, irrigation technology choice, and water productivity in Morocco. *Agricultural Water Management*. https://doi.org/10.1016/j.agwat.2026.110453
3. World Bank. (2017). *Managing urban water scarcity in Morocco*. https://doi.org/10.1596/29190
4. Bajja, S., Sackitey, G. M., & Hassanein, E. A. (2026). Determinants of agricultural productivity in Morocco: An empirical analysis of climatic, technological, and socioeconomic factors. *Environmental and Sustainability Indicators*. https://doi.org/10.1016/j.indic.2026.101369
5. Taheripour, F., Tyner, W. E., & Haqiqi, I. (2020). *Water scarcity in Morocco*. https://doi.org/10.1596/33306
6. Tekken, V., & Kropp, J. (2012). Climate-driven or human-induced: Indicating severe water scarcity in the Moulouya River basin (Morocco). *Water, 4*(4), 959–982. https://doi.org/10.3390/w4040959
7. Rijsberman, F. R. (2006). Water scarcity: Fact or fiction? *Agricultural Water Management, 80*(1–3), 5–22. https://doi.org/10.1016/j.agwat.2005.07.001
8. Sanad, H., Moussadek, R., & Dakak, H. (2024). Ecological and health risk assessment of heavy metals in groundwater within an agricultural ecosystem using GIS and multivariate statistical analysis (MSA): A case study of the Mnasra region, Gharb plain, Morocco. *Water, 16*(17), 2417. https://doi.org/10.3390/w16172417
9. Loudyi, D., Saghiry, S., & Bouhamid Alaoui, A. (2022). Analysis of reservoir sedimentation impact on water transfer systems for water scarcity alleviation in arid and semi-arid zones: Case studies from Morocco. https://doi.org/10.3850/iahr-39wc252171192022ss1079
10. Leijnse, M., Droppers, B., & Bierkens, M. (2023). Key drivers and pressures of water scarcity at global hotspots. https://doi.org/10.5194/egusphere-egu23-4956
11. Wang, Y., Cao, T., & Zhang, S. (2026). Long-term socioeconomic trends and climate variability as drivers of virtual water scarcity in China. *Environmental Research Letters*. https://doi.org/10.1088/1748-9326/ae4abd
12. Boston, K. R. (2024). Resolving water scarcity in Morocco. *Pell Scholars and Senior Theses*. https://doi.org/10.18275/pbe-v042-007
13. El Ajraoui, T. (2026). Visualizing water scarcity: A semiotic analysis of social awareness commercials in Morocco. *International Journal for Multidisciplinary Research*. https://doi.org/10.36948/ijfmr.2026.v08i02.73851
14. Santos Pereira, L., Oweis, T., & Zairi, A. (2002). Irrigation management under water scarcity. *Agricultural Water Management, 57*(3), 175–206. https://doi.org/10.1016/s0378-3774(02)00075-6

The full 34-entry reference list is in the manuscript under [`PUBLICATION/water_scarcity_morocco.pdf`](PUBLICATION/water_scarcity_morocco.pdf).

---

## 📜 License

- **Code:** MIT License (see [`LICENSE`](LICENSE))
- **Manuscript and documentation:** CC-BY-4.0

```
MIT License

Copyright (c) 2026 Samir Baladi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
```

---

## 👤 Author

**Samir Baladi**
Independent Interdisciplinary Researcher
Ronin Institute / Rite of Renaissance

| Contact | Link |
|---------|------|
| Email | gitdeeper@gmail.com |
| ORCID | [https://orcid.org/0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) |
| Zenodo | [https://doi.org/10.5281/zenodo.23884236](https://doi.org/10.5281/zenodo.23884236) |

---

<div align="center">

**Water Scarcity in Morocco · v1.0 · November 2026**

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23884236-1B4F72?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.23884236)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0003-8903-0029)
[![License: MIT](https://img.shields.io/badge/license-MIT-27ae60)](LICENSE)

*Exploratory Associational Analysis · Not Causally Validated*

</div>
