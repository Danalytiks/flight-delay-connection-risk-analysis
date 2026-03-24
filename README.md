# ✈️ Flight Delay & Connection Risk Analysis

## Overview

Missed flight connections are a major issue in air travel, impacting passenger experience and airline operations.

This project investigates the root causes of flight delays and their impact on connection risk using real-world U.S. flight data from 2024.

The insights generated here serve as the foundation for the **GateRunner** system — a decision-support tool designed to predict and mitigate missed connections.

---

## Problem Statement

Passengers often miss connecting flights due to unpredictable arrival delays.

Airlines and airports lack dynamic tools to assess connection feasibility in real time.

**Key challenge:**
> How can we predict delays and quantify their impact on connection risk?

---

## Objectives

- Identify the main causes of flight delays
- Quantify delay patterns across airlines, airports, and time
- Analyze how delays affect connection feasibility
- Provide data-driven insights for reducing missed connections

---

## Dataset

- Source: U.S. Flights Data (2024)
- Format: Parquet
- Includes:
  - Flight schedules
  - Arrival and departure delays
  - Delay causes (carrier, weather, NAS, etc.)

---

## Key Insights (to be updated)

- Late aircraft is a major driver of delays
- Delay propagation significantly impacts downstream flights
- Even moderate delays can lead to missed connections

---

## Proposed Solution

This analysis supports the development of **GateRunner**, which aims to:

- Predict arrival delays
- Estimate real connection time
- Simulate connection success probability
- Provide risk-based recommendations

---

## Project Structure

- `notebooks/` → Data analysis and exploration
- `README.md` → Project overview
- `requirements.txt` → Dependencies

---

## Next Steps

- Build delay prediction model
- Simulate connection scenarios
- Integrate results into GateRunner application
