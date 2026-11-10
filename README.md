# Customer Intelligence Platform
### Customer Segmentation, Churn Prediction & Customer Lifetime Value Analysis

An end-to-end Data Science and Machine Learning project that analyzes retail transaction data to understand customer purchasing behavior, identify valuable customer segments, estimate churn risk, and develop data-driven customer retention strategies.

## Live Application

**Try the deployed Customer Intelligence Platform:**

[Launch Customer Churn Prediction App](https://customer-intelligence-platform-mdbyhcvlf ehgbihuxtru9c.streamlit.app/)

The interactive application allows users to enter customer purchasing metrics and receive an estimated churn probability.

---

## Project Objectives

- Analyze historical retail transaction data to understand customer purchasing behavior.
- Segment customers using Recency, Frequency, and Monetary (RFM) analysis.
- Apply K-Means clustering to identify distinct customer groups.
- Develop machine learning models to estimate customer churn risk.
- Estimate Customer Lifetime Value (CLV) using historical purchasing behavior.
- Identify high-value customers and customers associated with churn risk.
- Develop actionable business recommendations to improve customer retention.

## Technologies Used

| Category | Tools and Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib |
| Machine Learning | Scikit-learn |
| Development Environment | Jupyter Notebook, VS Code |
| Business Intelligence | Power BI |
| Web Application | Streamlit |
| Model Persistence | Joblib |
| Version Control | Git, GitHub |

---

## Project Workflow

### 1. Data Cleaning and Exploratory Data Analysis

Used historical Online Retail transaction data to explore customer purchasing behavior.

Key activities:
- Inspected transaction records and data types.
- Handled missing values and invalid transaction records.
- Explored customer purchasing patterns.
- Analyzed revenue distribution and transaction frequency.
- Prepared customer-level data for segmentation and predictive modeling.

### 2. Customer Segmentation Using RFM Analysis

Applied RFM analysis to understand customer purchasing behavior.

The three RFM metrics:

- **Recency:** Number of days since the customer's last purchase.
- **Frequency:** Number of unique invoices associated with the customer.
- **Monetary:** Total amount spent by the customer.

Used K-Means clustering to identify customer groups.

The analysis identified two broad customer segments:

**High-Value / Loyal Customers**
- More recent purchases.
- Higher purchase frequency.
- Greater monetary contribution.

**At-Risk / Low-Engagement Customers**
- Longer periods since their last purchase.
- Lower purchase frequency.
- Lower monetary contribution.

### 3. Customer Churn Prediction

Developed and compared classification models to estimate customer churn risk.

Models evaluated:
- Logistic Regression
- Random Forest Classifier
- Balanced Logistic Regression

The selected preliminary model was **Balanced Logistic Regression**, using a classification threshold of 0.40.

#### Model Performance

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 58.19% |
| Precision | 47.59% |
| Recall | 87.04% |
| F1-score | 61.54% |
| ROC-AUC | 0.7050 |

The selected model prioritizes recall, helping identify a larger proportion of customers carrying the historical churn label.

This comes with a trade-off: lower precision means more customers who would not churn are also flagged as potential churn risks.

**Evaluation limitation:** The classification threshold was selected using the test set. Therefore, these results should be treated as preliminary rather than an independent final performance estimate. Further validation using a separate validation set and untouched holdout test set is recommended.

### 4. Customer Lifetime Value (CLV) Estimation

Estimated customer annualized spending using historical transaction data.

The dataset covered approximately 373 days (12.25 months).

Annualized customer value was calculated using:

Annualized Value = (Historical Customer Spending / Observation Months) × 12

Generated illustrative customer revenue projections for different relationship durations.

| Projection | Average Customer Value |
|---|---:|
| 1 Year | £1,287.12 |
| 2 Years | £2,574.25 |
| 3 Years | £3,861.37 |

The analysis also divided customers into four value segments:

- Low Value
- Medium Value
- High Value
- Premium Value

**CLV limitation:** These are simplified revenue-based projections assuming customers maintain their historical annualized spending rate. They do not account for customer retention probability, gross profit margins, acquisition costs, or discount rates.

### 5. Customer Churn and Revenue Analysis

Analyzed historical churn labels across customer value segments.

Key findings:

- Low Value customers had the highest historical churn rate at approximately 57.89%.
- Premium Value customers had the lowest historical churn rate at approximately 14.65%.
- Premium Value customers contributed approximately 75.6% of total historical revenue.
- Premium Value customers carrying a churn label of 1 represented approximately £280,816.71 in historical spending.

These findings demonstrate why customer retention strategies should consider both churn risk and financial contribution.

Historical revenue associated with churn-labelled customers should not be interpreted as confirmed lost revenue.

### 6. Business Recommendations

Based on customer segmentation, churn analysis, and estimated customer value, the following strategies were identified.

**Premium Value Customers**
- Prioritize personalized retention campaigns.
- Provide loyalty rewards and exclusive offers.
- Monitor purchasing behavior for signs of declining engagement.

**High Value Customers**
- Encourage repeat purchases through loyalty programs.
- Provide personalized product recommendations.
- Identify changes in purchasing frequency.

**Medium Value Customers**
- Use targeted promotions to encourage repeat purchases.
- Recommend complementary products.
- Monitor changes in purchasing activity.

**Low Value Customers**
- Use cost-effective email campaigns and automated engagement.
- Test limited-time discounts to encourage repeat purchases.
- Avoid disproportionately expensive retention incentives.

**Overall Business Insight:** Customer retention strategies should consider both estimated churn risk and customer financial contribution rather than relying on churn probability alone.

### 7. Power BI Dashboard

Developed an interactive Power BI dashboard to explore:

- Customer segmentation.
- Revenue distribution.
- Customer purchasing behavior.
- Recency and frequency patterns.
- Customer-level metrics.

Dashboard file: `Customer_Segmentation_Analytics.pbix`

### 8. Interactive Streamlit Application

Developed and deployed an interactive application using Streamlit.

The application accepts five customer features:

1. Recency
2. Purchase Frequency
3. Monetary Value
4. Total Quantity Purchased
5. Average Order Value

It uses the saved machine learning model and StandardScaler to generate:

- Estimated churn probability.
- Churn classification.
- Customer risk assessment.

The model uses a 0.40 decision threshold.

---

## Project Structure

```text
customer-intelligence-platform/
│
├── data/
│
├── models/
│   └── customer_churn_model.joblib
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── Customer_Segmentation_Analytics.pbix
```

## Run the Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/VaibhavKela/customer-intelligence-platform.git
```

### 2. Navigate to the project directory

```bash
cd customer-intelligence-platform
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Launch the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser at the local Streamlit address.

## Dataset

The project uses the Online Retail dataset containing historical transaction-level retail information.

The dataset is used to calculate customer-level purchasing metrics, perform RFM segmentation, and construct historical churn labels.

The original dataset is not included in this repository. Place the dataset in the appropriate `data/` directory before running the analysis notebook.

## Limitations and Future Improvements

- Validate churn predictions using an independent holdout dataset.
- Explore additional customer behavior features to improve predictive performance.
- Develop a more comprehensive CLV model incorporating retention probability and profit margins.
- Evaluate customer retention strategies using expected financial returns.
- Improve model calibration and threshold selection.
- Monitor model performance on new transaction data.

## Author

**Vaibhav Kela**

MS Computer Science Student  
Data Science | Machine Learning | Data Analytics

GitHub: [VaibhavKela](https://github.com/VaibhavKela)

LinkedIn: [Connect with me](https://www.linkedin.com/in/vaibhav-kela-860189230/)
