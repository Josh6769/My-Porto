import streamlit as st
import pandas as pd

# 👑 Layout Configuration
st.set_page_config(
    page_title="Yash Borade | Executive Portfolio", 
    page_icon="💼", 
    layout="centered"
)

# 👑 Premium Header Space using Native Streamlit Blocks
st.title("💼 Yash Borade")
st.subheader("Operations Analyst & Cross-Functional Project Specialist")
st.markdown("⚡ *Bridging Quantitative Engineering Logic with High-Conversion Business Systems | Ex-London Strategy*")

st.markdown("---")

# 🗂️ Interactive Project Selector (All 4 Case Studies Loaded)
project = st.selectbox(
    "Select Strategic Intervention Framework:", 
    [
        "1. The Jockey Club: Demographic Renewal Funnel", 
        "2. The Banc: International Operational Blueprint",
        "3. Margaret Howell: Cultural Distribution Strategy",
        "4. Glamira Luxury: Experiential Acquisition Funnel"
    ]
)

st.markdown("---")

# -------------------------------------------------------------
# CASE STUDY 1: THE JOCKEY CLUB
# -------------------------------------------------------------
if "The Jockey Club" in project:
    st.markdown("### 🎯 The Jockey Club: Demographic Renewal Funnel")
    st.caption("**Core Methodology:** McKinsey Problem-Solving + Human Experience Design")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Target Audience Reach", value="+45%", delta="Instagram Discovery Loop")
    with col2:
        st.metric(label="Systemic Retention", value="100% Core", delta="Wax-Sealed Table Handoff")

    st.markdown("#### **Systemic Interventions Implemented:**")
    st.markdown("* **Pillar 01 | The Hospitality Loop:** Re-engineered high-touch dining SOPs to eliminate track intimidation for under-35 demographics.")
    st.markdown("* **Pillar 02 | The Onboarding Trigger:** Anchored a physical, premium wax-sealed invite and betting voucher system directly to tables to eliminate entry friction.")
    st.info("💡 Strategic Verdict: Retention is an architecture problem, not a brand marketing problem.")

# -------------------------------------------------------------
# CASE STUDY 2: THE BANC
# -------------------------------------------------------------
elif "The Banc" in project:
    st.markdown("### 📈 The Banc: International Operational Blueprint")
    st.caption("**Core Methodology:** Cross-Functional Scaling & Data Governance")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Repeat Client Retention", value="+10%", delta="Coached Greeting Routine")
    with col2:
        st.metric(label="Staff Optimization", value="29 Personnel", delta="Streamlined Checklists")

    st.markdown("#### **Systemic Interventions Implemented:**")
    st.markdown("* **Workflow Governance:** Transformed chaotic peak-hour dining surges into high-fidelity, predictable customer journeys.")
    st.markdown("* **Operational Support:** Formulated and deployed structured weekday promotional playbooks across multi-location hubs (Tottenham, Enfield, Dubai).")
    st.success("⚡ Strategic Verdict: Scaled organic allure into a highly predictable, cross-border revenue engine.")

# -------------------------------------------------------------
# CASE STUDY 3: MARGARET HOWELL
# -------------------------------------------------------------
elif "Margaret Howell" in project:
    st.markdown("### 👔 Margaret Howell: Cultural Distribution Strategy")
    st.caption("**Core Methodology:** Radical Operational Transparency & Ecosystem Integration")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Target Demographic Focus", value="Under-35s", delta="Ecosystem Pipeline")
    with col2:
        st.metric(label="Brand Strategy Scope", value="Next-Gen", delta="Zero Value Dilution")

    st.markdown("#### **Systemic Interventions Implemented:**")
    st.markdown("* **Pillar 01 | Pipeline Architecture:** Engineered a structured university partnership framework to bridge heritage design values with young modern makers.")
    st.markdown("* **Pillar 02 | Process Documentation:** Dismantled traditional distribution barriers by introducing structured, open sustainability tracking updates.")
    st.warning("💡 Strategic Verdict: A brand perceived as old-world is rarely a product problem—it is a distribution and storytelling friction loop.")

# -------------------------------------------------------------
# CASE STUDY 4: GLAMIRA LUXURY
# -------------------------------------------------------------
else:
    st.markdown("### 💎 Glamira Luxury: Experiential Acquisition Funnel")
    st.caption("**Core Methodology:** Behavioral Psychology Funnel Design")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Base Conversion Driver", value="15% Discount", delta="Universal Participation")
    with col2:
        st.metric(label="Funnel Mechanism", value="UGC Engine", delta="High-Intent Bridal Capture")

    st.markdown("#### **Systemic Interventions Implemented:**")
    st.markdown("* **Psychological Hooking:** Constructed an experiential campaign framework (#GlamorousProposal) weaponizing viral social proof for premium conversions.")
    st.markdown("* **Pipeline Optimization:** Engineered a user-generated content funnel that automatically turns passive digital engagement into verified, high-margin customer acquisitions.")
    st.info("⚡ Strategic Verdict: Weaponizing customer psychology systematically turns casual interactions into a highly predictable pipeline.")

st.markdown("---")
st.caption("🔒 Secured Platform Module | Formulated for European & Domestic Technical Operations Vetting.")
