import streamlit as st
from workflows import app
from life_coach import provide_life_advice

# Streamlit app title
st.title("Fitness and Life Coach")


# User inputs
weight = st.number_input("Enter your weight (kg):", min_value=20.0, max_value=400.0)
gender = st.selectbox("Enter your gender:", ["Male", "Female", "Non-Binary", "Other"])
workout_goal = st.selectbox("Enter your workout goal:", ["Fat Loss", "Muscle Gain", "Mild Workout", "Strength Building", "Endurance Training", "Toning & Sculpting", "High-Intensity Training", "Athletic Performance", "General Fitness", "Stress Relief & Relaxation", "Balance & Stability", "Sports-Specific Training", "Weight Maintenance", "Core Strengthening"])


# Initialize state
state = {
    "weight": weight,
    "gender": gender,
    "workout_goal": workout_goal,
}

# Run the workflow when the user clicks the button
if st.button("Generate Plan"):
    if not weight or not gender or not workout_goal:
        st.error("Please fill in all fields.")
    else:
        # Proceed with generating the plan
        state = {
            "weight": weight,
            "gender": gender,
            "workout_goal": workout_goal,
        }
        fitness_result = app.invoke(state)

        # Display workout plan
        st.subheader("Workout Plan")
        st.write(fitness_result["workout_plan"])

        # Display calorie intake
        st.subheader("Daily Calorie Intake")
        st.write(f"{fitness_result['calorie_intake']} calories")

        # Display progress feedback
        st.subheader("Progress Feedback")
        st.write(fitness_result["adjustment"])



