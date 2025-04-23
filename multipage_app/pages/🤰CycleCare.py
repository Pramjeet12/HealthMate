import streamlit as st
import datetime
from datetime import timedelta

# Page Configuration
st.set_page_config(page_title="AI Menstrual Health Tracker", layout="centered")

st.title("AI-Powered Menstrual Health Tracker🌸")
st.markdown("Track your menstrual cycle, predict upcoming periods, and get personalized health tips.")

# Input Section
st.header("Enter Cycle Details📅")
with st.form("cycle_form"):
    last_period = st.date_input("Last Period Start Date", max_value=datetime.date.today())
    avg_cycle_length = st.number_input("Average Cycle Length (days)", min_value=21, max_value=35, value=28)
    period_duration = st.number_input("Period Duration (days)", min_value=2, max_value=10, value=5)
    submit = st.form_submit_button("Track My Cycle🩸")

if submit:
    today = datetime.date.today()
    days_passed = (today - last_period).days
    next_period_start = last_period + timedelta(days=avg_cycle_length)
    ovulation_day = last_period + timedelta(days=avg_cycle_length // 2)
    fertile_window_start = ovulation_day - timedelta(days=3)
    fertile_window_end = ovulation_day + timedelta(days=1)

    st.success("✅ Cycle Tracked Successfully!")

    st.subheader("🩸 Your Cycle Insights")
    st.markdown(f"- **Next Period Start:** {next_period_start.strftime('%d %B %Y')}")
    st.markdown(
        f"- **Fertile Window:** {fertile_window_start.strftime('%d %B')} to {fertile_window_end.strftime('%d %B')}")
    st.markdown(f"- **Ovulation Day:** {ovulation_day.strftime('%d %B')}")

    # Timeline summary
    st.subheader("📆 Cycle Timeline Overview")
    timeline = [
        ("Last Period", last_period),
        ("Next Period", next_period_start),
        ("Ovulation", ovulation_day),
        ("Fertile Window Start", fertile_window_start),
        ("Fertile Window End", fertile_window_end)
    ]

    for label, date in timeline:
        st.write(f"📍 {label}: {date.strftime('%A, %d %B %Y')}")

    # Health Tips Section
    st.subheader("Health Tips💡")
    st.markdown("""
    - Drink plenty of water and maintain a healthy diet.
    - Track symptoms like cramps, mood swings, or flow changes.
    - Consider iron-rich foods during your period.
    - For irregular cycles, consult a doctor or gynecologist.
    """)

# Footer
st.markdown("---")
st.caption(
    "⚠️Disclaimer: This tool provides general cycle predictions. Always consult a healthcare professional for medical advice.")
