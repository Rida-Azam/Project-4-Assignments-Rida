# Project 8: Create a Python Streamlit BMI Calculator Web App in Just 6 Minutes

# 🧮 BMI Calculator with Streamlit

import streamlit as st

# Page Config
st.set_page_config(page_title="BMI Calculator 🧘‍♀️", page_icon="💪", layout="centered")

# Title with Emoji
st.title("💪 Body Mass Index (BMI) Calculator")
st.markdown("### 🧘‍♂️ Let's find out how healthy you are!")

# Input Fields
height = st.number_input("📏 Enter your height (in meters):", min_value=0.5, max_value=2.5, step=0.01)
weight = st.number_input("⚖️ Enter your weight (in kilograms):", min_value=10.0, max_value=300.0, step=0.1)

# Button to calculate
if st.button("🧮 Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"🎯 Your BMI is: **{bmi:.2f}**")

        # Result Interpretation with emojis
        if bmi < 18.5:
            st.warning("🟡 You are **underweight**. 🥗 Try to maintain a balanced diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("🟢 You have a **normal** weight. 💚 Keep it up!")
        elif 25 <= bmi < 29.9:
            st.info("🔵 You are **overweight**. 🚶‍♂️ Consider regular exercise.")
        else:
            st.error("🔴 You are in the **obese** range. 🏥 It's a good idea to consult a healthcare provider.")
    else:
        st.error("⚠️ Please enter a valid height!")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
