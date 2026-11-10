@"
# Customer Intelligence Platform

### Customer Segmentation, Churn Prediction & Customer Lifetime Value Analysis

An end-to-end data science project focused on analyzing retail customer behavior, identifying customer segments, predicting churn risk, and estimating customer lifetime value.

## Project Objectives

- Perform customer segmentation using RFM analysis.
- Identify high-value and at-risk customers.
- Build machine learning models for churn prediction.
- Estimate Customer Lifetime Value (CLV).
- Develop business recommendations for customer retention.
- Build an interactive Streamlit application.

## Live Application

Try the deployed Customer Intelligence Platform:

[Open the Streamlit App](https://customer-intelligence-platform-mdbyhcvlfehgbihuxtru9c.streamlit.app/)

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Power BI
- Streamlit
- Git and GitHub

## Machine Learning

**Selected Model:** Balanced Logistic Regression

**Decision Threshold:** 0.40

| Metric | Score |
|---|---:|
| Accuracy | 58.19% |
| Precision | 47.59% |
| Recall | 87.04% |
| F1-score | 61.54% |
| ROC-AUC | 0.7050 |

The model prioritizes identifying potential churners, with higher recall at the cost of more false positives.

## Customer Segmentation

RFM analysis and K-Means clustering were used to identify two broad customer groups:

- High-Value / Loyal Customers
- At-Risk / Low-Engagement Customers

## Customer Lifetime Value

Estimated annualized customer spending and generated illustrative one-, two-, and three-year CLV projections using historical purchasing behavior.

## Power BI Dashboard

Created an interactive dashboard to analyze customer segments, purchasing patterns, and revenue distribution.

## Streamlit Application

The application allows users to enter five customer metrics and receive:

- Estimated churn probability
- Churn classification
- Customer risk assessment

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt