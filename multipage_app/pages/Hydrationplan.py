import streamlit as st

# Function to calculate recommended water intake
def calculate_water_intake(weight, activity_level):
    base_intake = weight * 0.033  # General rule: 33ml per kg
    if activity_level == "Low":
        return round(base_intake, 2)
    elif activity_level == "Moderate":
        return round(base_intake * 1.2, 2)
    else:
        return round(base_intake * 1.5, 2)

# Streamlit UI
st.title("Hydration & Water Intake Tracker💧")

# User Inputs
weight = st.number_input("Enter Your Weight (kg)⚖️", min_value=20, max_value=200, step=1)
activity_level = st.selectbox("Select Your Activity Level🏃", ["Low", "Moderate", "High"])
water_intake = st.number_input("Enter Your Today's Water Intake (liters)🥤", min_value=0.0, max_value=10.0, step=0.1)

# Button to generate results
if st.button("Check Hydration Status💡"):
    if weight:
        recommended_intake = calculate_water_intake(weight, activity_level)
        st.subheader(f"💡 Recommended Daily Water Intake: **{recommended_intake} liters**")

    # Check user progress
    if water_intake:
        if water_intake < recommended_intake:
            st.warning("⚠️ You're not drinking enough water! Try to stay hydrated.")
        elif water_intake > recommended_intake:
            st.success("✅ Great! You're well-hydrated.")
        else:
            st.info("👍 Perfect! You're meeting your hydration goal.")

    # Hydration Tips
    st.subheader("💡 Hydration Tips:")
    st.write("- Aim to drink **small amounts** throughout the day instead of large quantities at once.")
    st.write("- **Carry a water bottle** with you to make hydration a habit.")
    st.write("- **Increase water intake** if you're sweating a lot due to workouts or hot weather.")
    st.write("- Try **flavored water** (lemon, mint, cucumber) if you find plain water boring.")

    # Progress Bar for Visual Tracking
    progress = min(water_intake / recommended_intake, 1.0)
    st.progress(progress)

    st.write("💙 Stay Hydrated & Stay Healthy! 💙")
