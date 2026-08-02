import os 
import streamlit as st
from openai import OpenAI

# ------------------ NVIDIA API ------------------

client = OpenAI(
    api_key="NVIDIA_API_KEY",
    base_url="https://integrate.api.nvidia.com/v1")
    
st.title("🔢 Simple Calculator")

# 1. Inputs for two numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# 2. Dropdown for selecting the operation
operation = st.selectbox("Select operation", ["+", "-", "*", "/"])

# 3. Button to compute and show the result
if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."

    # Display the result
    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"**Result:** {result}")