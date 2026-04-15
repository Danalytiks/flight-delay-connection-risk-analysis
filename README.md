# ✈️ GateRunner — Flight Connection Risk Analysis

> **Motivation:** Having worked at Munich Airport, I witnessed firsthand how
> disorienting and stressful missed connections can be for passengers. This
> project combines that operational experience with data science to understand
> the problem at scale — and build toward a solution.

---

## Overview

This project analyzes U.S. domestic flight delay data from 2024 to understand
the main drivers of delays and their impact on passenger connection risk.

The analysis combines exploratory data analysis, risk segmentation, feature
engineering, and machine learning to investigate how factors such as airline,
airport, route, and time of day influence the probability of missed connections.

This project serves as the analytical foundation for **GateRunner** — a
passenger guidance concept designed to reduce the stress and confusion of
tight connections at airports.

---

## Business Problem

Missed flight connections are a major operational and passenger experience
issue in air travel. When delays occur — especially severe ones — passengers
face a stressful and disorienting situation: they don't know if they will make
it, where to go, or how much time they have.

Even when most flights operate within acceptable limits, a smaller number of
severe delays can significantly disrupt passenger itineraries and increase
operational complexity for airlines.

---

## Objectives

- Analyze the distribution and causes of flight delays
- Identify high-risk patterns by airline and airport
- Segment flights into connection risk categories (SAFE / TIGHT / RISKY)
- Build and compare multiple machine learning models to predict connection risk
- Evaluate the trade-off between predictive accuracy and real-world feature availability
- Connect the results to a real-world product concept: **GateRunner**

---

## Dataset

- **Source:** U.S. Bureau of Transportation Statistics (BTS)
- **Period:** 2024
- **Size:** 10,000 flights (sample from full dataset)
- **Features:** 35 variables including airline, origin, destination,
  scheduled/actual times, and delay causes

---

## 🔍 Key Insights

- **20.4% of flights** are delayed more than 15 minutes (1 in 5 flights)
- **7.7% of flights** are delayed more than 60 minutes (high risk of missed connection)
- Delays are not random — they are **systematic and predictable**
- **Late aircraft delay** is the main driver of disruption
- Certain airlines and airports show consistently higher risk patterns

### Detailed Findings

| Finding | Value |
|---|---|
| Flights delayed > 15 min | **~20.4%** — 1 in 5 flights |
| Flights delayed > 60 min (RISKY) | **~7.7%** — high missed connection risk |
| Primary cause of delays | **Late aircraft propagation** (cascading delays) |
| Most reliable airline | **HA** (Hawaiian Airlines) |
| Highest risk airline | **F9, G4** — nearly 1 in 5 flights RISKY |
| Highest risk airports | **IAD, DEN** — over 20% of flights RISKY |

### Risk Segmentation

| Category | Definition | Share of Flights |
|---|---|---|
| ✅ SAFE | Arrival delay ≤ 15 min | ~78% |
| ⚠️ TIGHT | 15 min < delay ≤ 60 min | ~14% |
| 🔴 RISKY | Arrival delay > 60 min | ~7.7% |

---

## ⚖️ Model Comparison: Performance vs Realism

Two models were evaluated:
- **Model A:** includes `dep_delay` (high predictive power)
- **Model B:** excludes `dep_delay` (realistic pre-departure scenario)

| Model | Macro F1 |
|---|---|
| With `dep_delay` | ~0.82 |
| Without `dep_delay` — Baseline | ~0.30 |
| Without `dep_delay` — Feature Engineering | ~0.43 |
| Without `dep_delay` — Binary (SAFE vs AT RISK) | ~0.59 |

### Key Takeaway

`dep_delay` is a dominant predictor of connection risk.
However, it introduces **data leakage**, since it may not be available before departure.

This reveals a critical trade-off between:
- **Model accuracy**
- **Real-world applicability**

The binary engineered model (F1 = 0.59) uses only pre-departure features
and represents the most realistic baseline for a production system.

---

## Feature Engineering

New features created from pre-departure data to improve the model:

| Feature | Description |
|---|---|
| `dep_hour` | Hour of day from scheduled departure time |
| `is_weekend` | Binary flag for Saturday / Sunday |
| `carrier_risk_rate` | Historical RISKY rate per airline |
| `route_risk_rate` | Historical RISKY rate per origin–destination pair |

---

## Model Progression

```
Baseline (3-class)     →  F1: 0.30
+ Feature Engineering  →  F1: 0.43  (+43%)
+ Binary Classification →  F1: 0.59  (+97% vs baseline)
```

The most impactful improvement came from reframing the problem as binary
classification (SAFE vs AT RISK), which is also more actionable for a
real-world passenger decision tool.

---

## 🚀 Why This Matters

This project goes beyond model performance.

It shows how data science can:
- Identify operational risk patterns
- Support real-time decision-making
- Bridge analysis and product design

It also demonstrates how **domain knowledge** (aviation) can significantly
enhance data science solutions.

This work directly supports the concept behind **GateRunner**, turning real
operational problems into data-driven tools.

---

## GateRunner Connection

This project serves as the analytical foundation for **GateRunner** — a
proposed passenger guidance tool for airports.

**The core idea:** When a passenger lands with a tight connection, GateRunner
answers one question instantly:

> *"You have X minutes. Your gate is Y. Here is how to get there."*

The analysis proves that:
1. The problem is **real and measurable** (20% of flights delayed)
2. Risk patterns are **predictable** (certain airlines/airports are consistently worse)
3. A pre-departure model is **feasible** (F1 = 0.59 without real-time data)

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python / Pandas | Data manipulation |
| Matplotlib / Seaborn | Visualization |
| Scikit-learn | ML models & evaluation |
| XGBoost | Gradient boosting classifier |
| Joblib | Model persistence |
| Jupyter Notebook | Analysis environment |

---

## Repository Structure

```
flight-delay-connection-risk-analysis/
├── Flight_delays_EDA_EN.ipynb     # Full analysis & modeling (English)
├── Flight_delays_EDA_PT.ipynb     # Full analysis & modeling (Portuguese)
├── models/
│   ├── model_binary.joblib        # Trained binary model
│   ├── carriers.joblib            # Airline list
│   ├── airports.joblib            # Airport list
│   ├── features.joblib            # Feature list
│   ├── carrier_risk_map.joblib    # Carrier risk rates
│   └── route_risk_map.joblib      # Route risk rates
├── flight_data_2024_data_dictionary.csv
└── README.md
```

---

## Next Steps

- [ ] Integrate real-time flight status API
- [ ] Add airport navigation guidance (GateRunner core feature)
- [ ] Expand feature engineering with weather and congestion data
- [ ] Train on full BTS dataset (not just sample)
- [ ] Deploy GateRunner app publicly via Streamlit Cloud
- [ ] Expand to international airports (starting with MUC)

---

## About

Built by **Daniela Costa Glotzbach** as part of a Data Science career transition.

Background in airport operations (Munich Airport) combined with data science
training to address a real-world passenger experience problem.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/danalytiks)
[![GitHub](https://img.shields.io/badge/GitHub-Danalytiks-black?logo=github)](https://github.com/Danalytiks)
