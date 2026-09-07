import streamlit as st
from google import genai

import os
from dotenv import load_dotenv

# Load environment variables from your local .env file
load_dotenv()

# Safely fetch the key
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="AI Expense Analyser",
    layout="centered"
)

st.title("AI Expense Analyser")

st.write(
    "Enter your monthly expenses and get an AI-generated "
    "expense analysis with saving suggestions."
)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=0.0,
    value=30000.0
)

expense_details = st.text_area(
    "Enter Your Expenses",
    placeholder="""Example:

Rent: 10000
Food: 5000
Travel: 3000
Shopping: 4000
Electricity Bill: 1500
Entertainment: 2000
""",
    height=280
)

analysis_type = st.selectbox(
    "Select Analysis Type",
    [
        "Basic Expense Analysis",
        "Saving Suggestions",
        "Budget Improvement Plan",
        "Complete Financial Summary"
    ]
)

if st.button(
    "Analyse Expenses",
    type="primary",
    use_container_width=True
):

    if expense_details.strip() == "":
        st.warning("Please enter your expense details.")

    else:
        prompt = f"""
You are a personal expense analysis assistant.

Analyse the following monthly income and expense details.

Monthly Income:
{monthly_income}

Expense Details:
{expense_details}

Analysis Type:
{analysis_type}

Instructions:
- Calculate the total expenses.
- Calculate the remaining balance.
- Identify the highest expense category.
- Explain where the user is spending more.
- Give practical saving suggestions.
- Create a suitable monthly budget.
- Use clear and beginner-friendly language.
- Display important values in Indian rupees.
- Do not provide investment or legal advice.
- Return only the expense analysis.
"""

        with st.spinner("Analysing your expenses..."):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        st.success("Expense analysis completed.")

        st.subheader("Expense Analysis")

        st.markdown(response.text)
