import streamlit as st
import pandas as pd

# Page Configuration for Phone-Scannable Layout
st.set_page_config(page_title="Yash Borade | Portfolio", layout="centered")

st.title("📊 Yash Borade | Systems Optimization Portfolio")
st.caption("Bridging Analytical Engineering with Revenue Optimization")

# Project Directory Selector
project = st.selectbox("Select Strategic Intervention Case Study:", 
                       ["The Jockey Club: Renewal Funnel", "The Banc: Operations Scale-up"])

if project == "The Jockey Club: Renewal Funnel":
    st.subheader("🎯 Demographic Renewal Funnel")
    st.markdown("**Framework Applied:** McKinsey Problem-Solving + Human Experience Design")
    
    # Quantitative Impact Metrics Dataframe
    metrics_data = {
        "Funnel Stage": ["Digital Instagram Discovery", "Hospitality Loop Onboarding", "Voucher Retention"],
        "Conversion Optimization Metric": ["+45% Reach Growth", "10% Retention Architecture", "Frictionless Table Handoff"]
    }
    df = pd.DataFrame(metrics_data)
    st.table(df)
    
    st.info("💡 Strategic Verdict: Retention is an architecture problem, not a brand marketing problem.")

elif project == "The Banc: Operations Scale-up":
    st.subheader("📈 International Operational Blueprint")
    st.markdown("**Core Action:** Re-engineered chaotic peak-hour dining systems into high-fidelity workflows.")
    
    metrics_data = {
        "Area Restructured": ["Peak-Hour Staff Coordination", "Guest Greeting Routine", "Shift Handover Systems"],
        "Operational Impact": ["Managed Team of 29 Staff", "10% Repeat Client Retention Boost", "Streamlined Checklists Plan"]
    }
    df = pd.DataFrame(metrics_data)
    st.table(df)
    st.success("⚡ Result: Scaled organic allure into a highly predictable revenue engine.")
