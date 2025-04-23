import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="🤰 Pregnancy Care & Nutrition", layout="centered")

st.title("AI-Powered Pregnancy Care & Nutrition Guide🤰")
st.markdown("Track your pregnancy stage, get trimester-wise tips, and receive personalized nutrition guidance.")

# Input Section
st.header("Enter Your Pregnancy Details🌸")

with st.form("pregnancy_form"):
    lmp = st.date_input("Last Menstrual Period (LMP)🩸", max_value=date.today())

    conception_date = st.date_input("Conception Date (if known)🧬", value=lmp, max_value=date.today())
    usg_date = st.date_input("Early Ultrasound Date (if done)🖥️", value=lmp, max_value=date.today())
    gest_age_weeks = st.number_input("Gestational Age at Ultrasound (weeks)📏", min_value=0, max_value=20, value=0)

    submit = st.form_submit_button("Get My Pregnancy Insights🧾")

# Processing Logic
if submit:
    today = date.today()
    gestational_age_days = None
    estimated_conception_date = None

    if gest_age_weeks > 0 and usg_date:
        # Use ultrasound if provided
        gest_age_at_usg = timedelta(weeks=gest_age_weeks)
        estimated_conception_date = usg_date - gest_age_at_usg + timedelta(days=14)
        gestational_age_days = (today - estimated_conception_date).days + 14
        method_used = "Ultrasound Scan"
    elif conception_date and conception_date != lmp:
        # Use conception date
        gestational_age_days = (today - conception_date).days + 14
        method_used = "Conception Date"
    else:
        # Fallback to LMP
        gestational_age_days = (today - lmp).days
        method_used = "LMP"

    gest_weeks = gestational_age_days // 7
    due_date = lmp + timedelta(days=280)

    # Determine Trimester
    if gest_weeks < 13:
        trimester = "First Trimester"
    elif 13 <= gest_weeks < 27:
        trimester = "Second Trimester"
    else:
        trimester = "Third Trimester"

    # Display Insights
    st.success("🍼 Pregnancy Details Generated!")
    st.markdown(f"- **Gestational Age:** {gest_weeks} weeks")
    st.markdown(f"- **Estimated Due Date (EDD):** {due_date.strftime('%d %B %Y')}")
    st.markdown(f"- **Current Trimester:** {trimester}")
    st.caption(f"📌 Calculated using: **{method_used}**")

    # Nutrition & Care Tips
    st.subheader("🥗 Nutrition & Care Tips")

    if trimester == "First Trimester":
        st.markdown("""
        - Eat folate-rich foods (e.g., spinach, oranges, fortified cereals).
        - Avoid alcohol, smoking, and excess caffeine.
        - Stay hydrated and get enough rest.
        """)
    elif trimester == "Second Trimester":
        st.markdown("""
        - Increase iron and calcium intake (e.g., dairy, leafy greens, lean meats).
        - Gentle exercise like walking or prenatal yoga is helpful.
        - Monitor fetal movements and visit your doctor regularly.
        """)
    elif trimester == "Third Trimester":
        st.markdown("""
        - Prioritize protein and iron-rich foods.
        - Stay active and do breathing/relaxation exercises.
        - Prepare a birth plan and pack your hospital bag.
        """)

    st.markdown("---")
    st.caption(
        "📌Note: This tool provides general guidance. Always consult a gynecologist or nutritionist for personalized advice.")
