import streamlit as st
from datetime import date

dob = st.date_input(
    "Select DOB",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

if st.button("Calculate Age"):
    today = date.today()

    diff = today - dob  # this gives total days

    years = diff.days // 365
    remaining_days = diff.days % 365

    st.write(f"Your age is {years} years and {remaining_days} days")