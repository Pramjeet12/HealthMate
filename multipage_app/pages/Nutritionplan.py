import streamlit as st


# Function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height to meters
    return round(weight / (height_m ** 2), 2)


# Function to generate meal plan
def generate_meal_plan(goal, activity_level):
    meal_plans = {
        "Weight Loss": {
            "Low": [
                "🥗 Breakfast: Oatmeal with fruits & nuts",
                "🥙 Lunch: Grilled chicken with quinoa & veggies",
                "🥦 Dinner: Steamed fish with greens & brown rice",
                "🍎 Snacks: Greek yogurt, almonds, or an apple"
            ],
            "Moderate": [
                "🥑 Breakfast: Scrambled eggs with whole wheat toast",
                "🥗 Lunch: Chicken salad with olive oil dressing",
                "🍲 Dinner: Lentil soup with a side of veggies",
                "🥜 Snacks: Hummus with carrot sticks, mixed nuts"
            ],
            "High": [
                "🍳 Breakfast: Boiled eggs, avocado, and whole-grain toast",
                "🍛 Lunch: Grilled salmon with roasted veggies",
                "🥗 Dinner: Stir-fried tofu with brown rice",
                "🍓 Snacks: Smoothie with banana, peanut butter, and chia seeds"
            ]
        },
        "Muscle Gain": {
            "Low": [
                "🍳 Breakfast: Scrambled eggs with whole wheat toast",
                "🥩 Lunch: Grilled chicken with sweet potatoes",
                "🍲 Dinner: Beef stew with quinoa",
                "🥜 Snacks: Protein shake, mixed nuts, cottage cheese"
            ],
            "Moderate": [
                "🍞 Breakfast: Peanut butter toast with banana",
                "🥗 Lunch: Chicken wrap with Greek yogurt dressing",
                "🍣 Dinner: Grilled salmon with wild rice",
                "🍌 Snacks: Protein smoothie, almonds, boiled eggs"
            ],
            "High": [
                "🥑 Breakfast: Avocado toast with eggs",
                "🥩 Lunch: Lean steak with roasted vegetables",
                "🥗 Dinner: Chicken stir-fry with brown rice",
                "🍫 Snacks: Cottage cheese with honey & nuts"
            ]
        },
        "Balanced Diet": {
            "Low": [
                "🍞 Breakfast: Whole grain toast with peanut butter",
                "🍛 Lunch: Lentil soup with whole wheat bread",
                "🥗 Dinner: Baked fish with mixed vegetables",
                "🍎 Snacks: Fruits, yogurt, and almonds"
            ],
            "Moderate": [
                "🍳 Breakfast: Scrambled eggs with spinach",
                "🍲 Lunch: Chicken & veggie stir-fry with brown rice",
                "🥗 Dinner: Tofu & quinoa salad",
                "🍉 Snacks: Hummus with cucumber, nuts, and dark chocolate"
            ],
            "High": [
                "🥑 Breakfast: Avocado smoothie with chia seeds",
                "🥩 Lunch: Grilled chicken with sweet potatoes & greens",
                "🍛 Dinner: Baked salmon with wild rice",
                "🍓 Snacks: Greek yogurt with berries & flaxseeds"
            ]
        }
    }
    return meal_plans[goal][activity_level]


# Streamlit UI
st.title("AI-Powered Diet & Nutrition Planner🥗")

# User Inputs
weight = st.number_input("Enter Your Weight (kg)⚖️", min_value=20, max_value=200, step=1)
height = st.number_input("Enter Your Height (cm)📏", min_value=100, max_value=250, step=1)
age = st.number_input("Enter Your Age🎂", min_value=10, max_value=100, step=1)
activity_level = st.selectbox("Select Your Activity Level🏃", ["Low", "Moderate", "High"])
goal = st.selectbox("Select Your Dietary Goal🎯", ["Weight Loss", "Muscle Gain", "Balanced Diet"])

# Button to generate meal plan
if st.button("Generate My Meal Plan💡"):
    if weight and height:
        bmi = calculate_bmi(weight, height)
        st.subheader(f"📊 Your BMI: **{bmi}**")

        # Health interpretation based on BMI
        if bmi < 18.5:
            st.warning("🔹 You are underweight. Consider a high-protein and calorie-dense diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ Your BMI is normal. Maintain a balanced diet and regular exercise.")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are overweight. A healthy calorie deficit may help.")
        else:
            st.error("🚨 You are in the obese range. Focus on a nutrient-rich, calorie-controlled diet.")

        # Display Meal Plan
        meal_plan = generate_meal_plan(goal, activity_level)
        st.subheader(f"🍽️ Your Personalized {goal} Meal Plan:")
        for meal in meal_plan:
            st.write(meal)

        # Healthy Tips
        st.subheader("💡 Nutrition Tips:")
        st.write("- Drink at least **2-3 liters of water** daily.")
        st.write("- Include **lean proteins, healthy fats, and fiber** in your meals.")
        st.write("- Avoid **processed foods and excess sugar.**")
        st.write("- **Meal prep** ahead to stay consistent with your goals.")
        st.write("🥦 **Stay Healthy & Eat Smart!** 🥑")
