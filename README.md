# ✈️ Flight Delay & Connection Risk Analysis

## Overview

This project analyzes U.S. domestic flight delay data from 2024 to understand the main operational drivers of delays and their impact on passenger connection risk.

The analysis combines exploratory data analysis and machine learning to investigate how factors such as airline, airport, route, and departure delays influence the probability of missed connections.

This project also supports the concept behind **GateRunner**, a decision-support tool designed to estimate connection risk in real time.

---

## Business Problem

Missed flight connections are a major operational and passenger experience issue in air travel.

Even when most flights operate within acceptable limits, a smaller number of severe delays can significantly disrupt passenger itineraries and increase operational complexity.

The goal of this project is to identify delay patterns, quantify connection risk, and build a predictive model that can support better decision-making.

---

## Objectives

- Analyze the distribution and causes of flight delays
- Identify high-risk patterns by airline and airport
- Segment flights into connection risk categories
- Build a machine learning model to predict connection risk
- Connect the results to a real-world product concept: **GateRunner**

---

## Dataset

This project analyzes U.S. domestic **flight delays from 2024** to understand connection risk and evaluate whether missed connections can be predicted before departure. It combines exploratory data analysis, risk segmentation, and machine learning, and supports the product logic behind GateRunner.

Key characteristics:
- 2024 domestic flight data
- Delay causes included
- Cleaned and standardized column names
- Binary cancellation/diversion indicators
- Delay-related missing values handled in preprocessing

For performance reasons, this notebook uses the provided sample dataset during exploratory analysis and model development.

---

## Key Insights

- Approximately **20.4%** of flights experienced significant arrival delays greater than 15 minutes
- About **7.57%** of flights showed severe delays greater than 60 minutes
- Delay propagation was a major factor, with **departure delay** being the most important predictor in the model
- Delay risk varies significantly across airlines and airports
- Operational risk is better captured through **SAFE / TIGHT / RISKY** segmentation than by average delay alone

---

## Modeling

A Random Forest Classifier was used to predict connection risk categories:

- **SAFE**
- **TIGHT**
- **RISKY**

### Model Performance
- Accuracy: **90%**

### Main Finding
The most important feature was:

- `dep_delay`

This suggests that delay propagation is a key mechanism behind missed connections.

---

## GateRunner Connection

This project supports the logic behind **GateRunner**, a proposed real-time connection risk tool.

The analysis shows that connection risk can be estimated from operational variables such as:
- departure delay
- airline
- airport
- route
- flight distance

This makes it possible to move from descriptive analysis to predictive decision support in aviation operations.

---

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Repository Contents

- `Flight_delays.ipynb` — full exploratory analysis and modeling workflow
- `flight_data_2024_data_dictionary.csv` — dataset column reference
- `README.md` — project overview

---

## Future Improvements

- Train the model on the full dataset
- Test additional classification models
- Add feature engineering for time blocks and airport volume
- Build an interactive dashboard
- Integrate the logic into the GateRunner application
