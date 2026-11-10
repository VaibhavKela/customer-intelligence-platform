
import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
    .main-title {
        font-size: 34px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .subtitle {
        color: #9CA3AF;
        font-size: 16px;
        margin-bottom: 25px;
    }
    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 15px;
    }
    div[data-testid="stMetric"] {
        background-color: rgba(128, 128, 128, 0.08);
        padding: 16px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# 2. LOAD TRAINED MODEL
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "customer_churn_model.joblib"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    artifacts = load_model()

    model = artifacts["model"]
    scaler = artifacts["scaler"]
    threshold = artifacts["threshold"]
    features = artifacts["features"]

except FileNotFoundError:
    st.error("Model file not found. Check the models folder.")
    st.stop()


# --------------------------------------------------
# 3. SIDEBAR
# --------------------------------------------------

st.sidebar.title("📊 Customer Intelligence")

st.sidebar.write("Customer Segmentation & Churn Prediction")

st.sidebar.divider()

st.sidebar.subheader("About this project")

st.sidebar.write(
    """
    This application uses machine learning to estimate
    customer churn probability from historical purchasing
    behavior.
    """
)

st.sidebar.subheader("Model Information")

st.sidebar.write("**Algorithm:** Balanced Logistic Regression")
st.sidebar.write(f"**Decision threshold:** {threshold:.0%}")
st.sidebar.write("**Features:** 5 customer metrics")

st.sidebar.divider()

st.sidebar.caption(
    "Developed as a Data Science portfolio project."
)


# --------------------------------------------------
# 4. MAIN DASHBOARD HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze customer behavior and identify potential churn risks.</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# 5. CUSTOMER INPUT SECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Customer Information</div>',
    unsafe_allow_html=True
)

st.write("Enter the customer's historical purchasing metrics.")

with st.form("customer_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        recency = st.number_input(
            "Recency (days)",
            min_value=0,
            value=25
        )

    with col2:
        frequency = st.number_input(
            "Purchase Frequency",
            min_value=0,
            value=8
        )

    with col3:
        monetary = st.number_input(
            "Total Monetary Value (£)",
            min_value=0.0,
            value=4500.0
        )

    col4, col5 = st.columns(2)

    with col4:
        total_quantity = st.number_input(
            "Total Quantity Purchased",
            min_value=0,
            value=120
        )

    with col5:
        average_order_value = st.number_input(
            "Average Order Value (£)",
            min_value=0.0,
            value=562.5
        )

    predict_button = st.form_submit_button(
        "Predict Customer Churn",
        type="primary",
        use_container_width=True
    )


# --------------------------------------------------
# 6. PREDICTION
# --------------------------------------------------

if predict_button:

    customer_data = pd.DataFrame([{
        "Recency": recency,
        "Frequency": frequency,
        "Monetary": monetary,
        "Total_Quantity": total_quantity,
        "Average_Order_Value": average_order_value
    }])

    customer_data = customer_data[features]

    scaled_data = scaler.transform(customer_data)

    churn_probability = model.predict_proba(scaled_data)[0, 1]

    churn_prediction = int(churn_probability >= threshold)

    st.divider()

    st.markdown(
        '<div class="section-title">Prediction Results</div>',
        unsafe_allow_html=True
    )

    # Summary metrics
    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:
        st.metric(
            "Churn Probability",
            f"{churn_probability * 100:.2f}%"
        )

    with result_col2:
        st.metric(
            "Classification",
            "Likely to Churn" if churn_prediction else "Unlikely to Churn"
        )

    with result_col3:
        st.metric(
            "Decision Threshold",
            f"{threshold:.0%}"
        )

    # Visual probability indicator
    st.subheader("Churn Risk Indicator")

    st.progress(float(churn_probability))

    st.caption(
        "The indicator represents the model's estimated churn probability."
    )

    # Risk interpretation
    st.subheader("Customer Risk Assessment")

    if churn_probability < 0.20:
        risk_level = "Low"
        st.success("Low estimated churn risk")

    elif churn_probability < threshold:
        risk_level = "Moderate"
        st.warning("Moderate estimated churn risk")

    else:
        risk_level = "High"
        st.error("High estimated churn risk")

    st.caption(
        "Low, Moderate, and High are descriptive probability bands. "
        "The model's actual classification cutoff remains 40%."
    )

    # Business recommendations
    st.subheader("Suggested Retention Actions")

    if churn_prediction == 1:

        st.write(
            """
            Consider the following retention actions:
            - Review the customer's recent purchasing activity.
            - Send a personalized re-engagement campaign.
            - Consider a targeted discount or loyalty incentive.
            - Monitor whether the customer makes another purchase.
            """
        )

    elif risk_level == "Moderate":

        st.write(
            """
            Consider these engagement actions:
            - Send personalized product recommendations.
            - Share relevant promotions and new arrivals.
            - Encourage repeat purchases through loyalty benefits.
            """
        )

    else:

        st.write(
            """
            Suggested actions:
            - Maintain the existing customer relationship.
            - Provide relevant product recommendations.
            - Continue regular engagement without unnecessary discounts.
            """
        )

    # Customer input summary
    with st.expander("View Customer Input Summary"):

        st.dataframe(
            customer_data,
            use_container_width=True,
            hide_index=True
        )


# --------------------------------------------------
# 7. FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Customer Intelligence Platform | Machine Learning Portfolio Project"
)
