# 📊 Flight Delay & Connection Risk Analysis

> Data analysis of 10 million US domestic flights to validate airport connection risk thresholds — the analytical foundation behind [GateRunner](https://github.com/Danalytiks/Gaterunner).

---

## 🎯 Objective

Validate the risk classification model used in GateRunner by answering:

1. How often do passengers face tight or risky connections due to arrival delays?
2. Which airlines and origins pose the highest connection risk?
3. Are the Safe / Tight / Risky thresholds statistically justified?

---

## 📁 Dataset

| Field | Value |
|---|---|
| Source | US Bureau of Transportation Statistics |
| Period | January – December 2024 |
| Records | ~10,000,000 domestic flights |
| Tool | Power BI |

Key fields used: `fl_date`, `op_unique_carrier`, `origin`, `arr_delay`

---

## 🧮 Risk Classification Model

Each flight is classified based on its arrival delay:

| Category | Condition | Interpretation |
|---|---|---|
| 🟢 **SAFE** | arr_delay ≤ 20 min | Passenger has comfortable buffer |
| 🟡 **TIGHT** | 20 < arr_delay ≤ 35 min | Connection is at risk |
| 🔴 **RISKY** | arr_delay > 35 min | Connection likely missed |

---

## 📈 Key Findings

### Risk Distribution

| Category | Flights | Share |
|---|---|---|
| 🟢 SAFE | 7,800,000 | 77.96% |
| 🟡 TIGHT | 1,280,000 | 12.83% |
| 🔴 RISKY | 760,000 | 7.57% |

**~1 in 5 flights** results in a Tight or Risky connection scenario — confirming the real-world relevance of GateRunner.

---

### Average Arrival Delay

- **Overall average**: 7.55 min
- **Most delayed carriers**: AA, F9, OH, B6
- **Worst origin airports**: VCT, FLG, ADQ, SCK, MOT (avg delay > 100 min)

---

### Seasonal Trends

- **Peak delay period**: July 2024 — average arrival delay spiked to ~350 min
- **Lowest delay period**: January–March 2024
- Summer months consistently show the highest connection risk

---

### Airline Risk Ranking

| Carrier | Avg Arrival Delay | Risk Level |
|---|---|---|
| AA | High | 🔴 |
| F9 | High | 🔴 |
| OH | Medium-High | 🟡 |
| B6 | Medium | 🟡 |

---

## 💡 Implications for GateRunner

| Finding | GateRunner impact |
|---|---|
| 7.57% of flights are RISKY | App targets a real, significant segment |
| Summer peak delays | Future feature: seasonal risk adjustment |
| Origin matters | Future feature: route-based risk scoring |
| Carrier matters | Future feature: airline delay factor in risk calc |

---

## 🔗 Related Project

This analysis was created to validate the data model behind **GateRunner** — a React app that helps airport passengers navigate tight connections at Munich Airport (MUC).

👉 **[GateRunner — Live Demo](https://gaterunner.vercel.app)**
👉 **[GateRunner — GitHub](https://github.com/Danalytiks/Gaterunner)**

---

## 🛠️ Tools Used

- **Power BI** — data modelling, DAX measures, interactive dashboard
- **US BTS dataset** — open flight data

---

## 👨‍💻 Author

**Daniela Costa Glotzbach** — Munich Airport (MUC) operations + Data Science

[![GitHub](https://img.shields.io/badge/GitHub-Danalytiks-181717?style=flat&logo=github)](https://github.com/Danalytiks)

---

*Part of the GateRunner project — turning airport data into better passenger experiences.* ✈️
