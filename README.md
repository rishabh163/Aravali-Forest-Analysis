# Aravali Forest Cover Analysis (2015–2021)

I'm Rishabh, a Python learner interested in data analysis and environmental issues. This project is part of my internship preparation and focuses on analyzing forest cover trends in Rajasthan's Aravali region.

---

## What I Tried to Do

There is a common discussion that forest cover in the Aravali region is decreasing. Instead of relying on opinions, I wanted to analyze official data myself and check whether the decline is statistically meaningful.

---

## Where I Got the Data

I used reports published by the Forest Survey of India (ISFR 2015, 2017, 2019, 2021).  

I manually went through the PDF reports, extracted district-wise forest cover percentages for 10 districts in the Aravali region of Rajasthan, and compiled them into a structured CSV file for analysis.

This process helped me understand how raw government data is transformed into an analyzable dataset.

---

## What I Found

| Metric                     | Value  |
|----------------------------|--------|
| Districts analyzed         | 10     |
| Mean forest cover (2015)   | 7.82%  |
| Mean forest cover (2021)   | 6.89%  |
| Absolute change            | -0.93% |
| Paired t-test p-value      | 0.0001 |
| Cohen’s d (effect size)    | 1.24   |

### Key Findings

- All 10 districts showed a decline in forest cover between 2015 and 2021.
- The paired t-test indicates that the decline is statistically significant (p < 0.05).
- The effect size (Cohen’s d = 1.24) suggests the decline is practically large.
- The overall trend shows a consistent reduction across districts during the study period.

*Note: Exact values may vary slightly depending on rounding. Run the script to see precise output.*

---

## Files in This Project

- `data/aravali_forest_data.csv` – cleaned dataset compiled from ISFR reports  
- `analysis.py` – Python script for analysis and visualization  
- `requirements.txt` – list of required Python libraries  

---

## How to Run My Code

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the analysis:

```bash
python analysis.py
```

---

## Tools Used

- Python 3
- pandas
- scipy
- matplotlib

---

## Limitations

- The dataset contains only four time points (2015–2021).
- Analysis is based on district-level aggregated data.
- More detailed spatial analysis using satellite imagery could provide deeper insights.

---

## About Me

Rishabh  
B.Tech Student | Interested in Data Analysis & AI  
(Open to internships and research opportunities)
