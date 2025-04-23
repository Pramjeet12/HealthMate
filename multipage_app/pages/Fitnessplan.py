import streamlit as st

# Function to generate health recommendations
def health_recommendations(hr, steps, sleep):
    recommendations = []

    # Heart Rate Analysis
    if hr > 100:
        recommendations.append("⚠️ **Your heart rate is high!** This may indicate stress or dehydration. Try deep breathing exercises, meditation, and ensure proper hydration.")
    elif hr < 60:
        recommendations.append("🔄 **Your heart rate is low!** If you feel dizzy, consider light exercises like walking or stretching to regulate it.")
    else:
        recommendations.append("✅ **Your heart rate is within a healthy range!** Keep maintaining a balanced lifestyle.")

    # Step Count Analysis
    if steps < 5000:
        recommendations.append("🚶 **You're not moving enough!** Try to take breaks and aim for at least 10,000 steps daily. Walking after meals improves digestion and heart health.")
    elif 5000 <= steps < 10000:
        recommendations.append("🏃 **Good job!** You're moderately active. Try adding some strength exercises or yoga to your routine.")
    else:
        recommendations.append("✅ **Excellent activity level!** Keep up the good work and ensure you allow recovery time to avoid fatigue.")

    # Sleep Analysis
    if sleep < 360:
        recommendations.append("😴 **You're not getting enough sleep!** Lack of sleep affects mood and metabolism. Try to get 7-8 hours per night.")
    elif 360 <= sleep < 420:
        recommendations.append("🌙 **Decent sleep, but could be better!** Consider improving sleep quality by reducing screen time before bed and maintaining a consistent schedule.")
    else:
        recommendations.append("✅ **Great sleep duration!** Keep following a consistent bedtime routine for overall health.")

    return recommendations

# Streamlit Web App
st.title("Personalized Health & Fitness Recommendations🏃")
st.write("Get **personalized insights** based on your **heart rate, step count, and sleep duration📊.**")

# User Inputs
hr = st.number_input("Enter Your Heart Rate (BPM)💓", min_value=30, max_value=200, step=1)
steps = st.number_input("Enter Your Daily Step Count🚶", min_value=0, max_value=50000, step=100)
sleep = st.number_input("Enter Your Sleep Duration (minutes)🛌", min_value=0, max_value=1440, step=10)

# Generate Recommendations Button
if st.button("Get Health Advice💡"):
    advice = health_recommendations(hr, steps, sleep)

    st.subheader("📌 Health & Fitness Recommendations:")
    for tip in advice:
        st.write("- " + tip)

    # Additional General Wellness Tips
    st.subheader("💡 Bonus Wellness Tips:")
    st.write("- **Stay Hydrated:** Drink at least 2-3 liters of water daily 💧")
    st.write("- **Manage Stress:** Try meditation, breathing exercises, or listening to calming music 🎵")
    st.write("- **Eat a Balanced Diet:** Include proteins, fiber, and healthy fats 🍎")
    st.write("- **Take Regular Breaks:** Avoid sitting for long periods – stretch and move every hour ⏳")

# Run the app with: streamlit run filename.py
