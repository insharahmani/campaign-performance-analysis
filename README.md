# Campaign Performance Analysis

## Objective

The objective of this project is to evaluate the performance of different marketing campaigns and identify which channels drive stronger positive customer responses. The analysis focuses on translating data insights into actionable business decisions.

---

## Business Question

**Which marketing campaigns have been most successful in driving positive customer responses, and which campaigns underperformed?**

Positive customer response is evaluated using revenue and units sold at the campaign level.

---

## Dataset Overview

The dataset contains client-level information including:

* Client characteristics (Client ID, Client Type, Number of Customers)
* Sales outcomes (Units Sold, Amount Collected)
* Marketing campaign indicators (Email, Flyer, Phone)
* Sales contact and competitive environment data

Each campaign column represents campaign activity intensity rather than a simple binary flag.

---

## Approach

1. Loaded and explored the dataset to understand structure and campaign indicators.
2. Treated a campaign as active when its value was greater than zero.
3. Analyzed each campaign separately by filtering campaign activity.
4. Aggregated campaign-level metrics.
5. Calculated key performance indicators.
6. Benchmarked campaign performance against overall averages.
7. Translated results into business decisions and recommendations.

---

## Key Performance Indicators (KPIs)

* **Total Units Sold** – Measures sales volume driven by each campaign.
* **Total Revenue** – Measures total monetary impact.
* **Customers Reached** – Unique clients exposed to each campaign.
* **Revenue per Customer** – Proxy for customer response quality.
* **Units Sold per Customer** – Indicates purchasing intensity.

---

## Key Insights

* Email campaigns generate the highest revenue per customer, indicating strong customer engagement and effective targeting.
* Flyer campaigns show moderate reach but lower conversion efficiency.
* Phone campaigns underperform in terms of revenue efficiency relative to effort.
* Campaign performance varies significantly, highlighting the importance of channel prioritization.

---

## Business Decisions

* **Scale Email campaigns** due to strong revenue efficiency.
* **Optimize or limit Flyer campaigns** to supporting roles.
* **Reduce or refine Phone campaigns**, focusing only on high-value customers.

---

## Impact Measurement (Proposed)

Although post-decision data is not available, impact can be measured using:

* Pre- and post-campaign revenue per customer comparison.
* Incremental lift analysis after reallocating budget.
* A/B testing between optimized and non-optimized campaigns.

---

## Tools Used

* Python
* pandas

---

## Files Included

* `campaign_analysis.py` – Python script for campaign performance analysis
* `Campaign-Data.csv` – Dataset (if permitted)
* `README.md` – Project overview and insights

---

## Summary

This analysis demonstrates how campaign-level data can be used to drive actionable business decisions. By combining KPI benchmarking with clear decision support and impact measurement logic, the project reflects a real-world analytics workflow rather than a purely descriptive analysis.
