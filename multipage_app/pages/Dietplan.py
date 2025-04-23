import streamlit as st


# Function to categorize BMI
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "⚠️ You need to gain healthy weight."
    elif 18.5 <= bmi <= 24.9:
        return "Normal", "✅ You have a healthy weight. Maintain your lifestyle."
    elif 25 <= bmi <= 29.9:
        return "Overweight", "⚠️ Consider reducing weight with a balanced diet and exercise."
    else:
        return "Obese", "❗ It's important to manage weight through diet and exercise."


# AI Diet Plan Function
def ai_diet_plan(bmi):
    if bmi < 18.5:
        return (
            "🍽️ Increase calorie intake with nutritious foods.\n"
            "- Include high-protein meals: Eggs, chicken, fish, tofu\n"
            "- Healthy fats: Avocado, nuts, olive oil\n"
            "- Complex carbs: Oats, sweet potatoes, whole grains"
        )
    elif 25 <= bmi <= 29.9:
        return (
            "🥗 Reduce calorie intake & choose high-fiber foods.\n"
            "- Eat more vegetables, lean proteins, and whole grains\n"
            "- Cut down on sugary foods and processed snacks\n"
            "- Drink plenty of water and avoid sugary drinks"
        )
    elif bmi >= 30:
        return (
            "⚠️ Prioritize weight management.\n"
            "- Focus on a **calorie deficit** diet\n"
            "- Eat **more fiber-rich foods** (vegetables, legumes, berries)\n"
            "- Avoid trans fats & processed sugars"
        )
    else:
        return (
            "🍎 Maintain a **balanced diet**.\n"
            "- Ensure you get **carbs, proteins, and healthy fats**\n"
            "- Eat a variety of fresh fruits and vegetables\n"
            "- Stay hydrated & eat home-cooked meals"
        )


# AI Workout Plan Function
def ai_workout_plan(activity_level, bmi):
    if activity_level == "Low":
        return (
            "🚶 **Beginner Workout Plan**\n"
            "- 30 min **brisk walking** daily\n"
            "- Try **light yoga & stretching**\n"
            "- Start **bodyweight exercises** (squats, push-ups)"
        )
    elif activity_level == "Moderate":
        return (
            "🏋️ **Intermediate Workout Plan**\n"
            "- **Strength training** 3-4x per week\n"
            "- **Cardio** (running, cycling) for 30 mins\n"
            "- **Core exercises** for muscle toning"
        )
    else:
        return (
            "🔥 **Advanced Workout Plan**\n"
            "- **High-intensity interval training (HIIT)**\n"
            "- **Strength & resistance training**\n"
            "- **Active recovery** (swimming, mobility drills)"
        )


# Streamlit Web App
st.title("AI-Driven Diet & Workout Plan🤖")
st.write("Get a **personalized health plan** based on your **BMI and activity level**📊.")

# User Inputs
bmi = st.number_input("Enter Your BMI⚖️", min_value=10.0, max_value=50.0, step=0.1)
activity_level = st.selectbox("Select Your Activity Level🏃", ["Low", "Moderate", "High"])

# Generate Recommendations Button
if st.button("Get AI Recommendations💡"):
    # Get BMI Category & Message
    category, message = bmi_category(bmi)

    # Get Recommendations
    diet_recommendation = ai_diet_plan(bmi)
    workout_plan = ai_workout_plan(activity_level, bmi)

    # Display BMI Info
    st.subheader("📊 BMI Analysis:")
    st.write(f"**Category:** {category}")
    st.write(f"**Advice:** {message}")

    # Display Diet Plan
    st.subheader("🍽️ Personalized Diet Plan:")
    st.write(diet_recommendation)

    # Display Workout Plan
    st.subheader("🏋️ Workout Plan:")
    st.write(workout_plan)

    # Additional Health Tips
    st.subheader("💡 Health & Wellness Tips:")
    st.write("- Maintain a **consistent sleep schedule** 🛏️")
    st.write("- Stay **hydrated** and drink at least 2-3 liters of water daily 💧")
    st.write("- Reduce **screen time** and take breaks from digital devices 📵")

# Run the app with: streamlit run filename.py

