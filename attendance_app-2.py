
import streamlit as st
import pandas as pd
from datetime import date
import os

# Constants
students = [f"Student {i}" for i in range(1, 31)]
teachers = [f"Teacher {i}" for i in range(1, 9)]
xlsx_path = "diary.xlsx"

# App title
st.title("📚 Daily Attendance Manager")
today = date.today()
selected_date = st.date_input("📅 Select Date", value=today)

# Placeholder for today's entries
all_entries = []

# Loop through 5 periods
for period in range(1, 6):
    st.header(f"Period {period}")
    col1, col2 = st.columns(2)

    # Select teacher for this period
    with col1:
        teacher = st.selectbox(f"👩‍🏫 Teacher for Period {period}", teachers, key=f"teacher_{period}")
    with col2:
        action = st.radio(f"Quick mark for Period {period}", ["None", "Mark All Present", "Mark All Absent"], key=f"quick_{period}")

    # Student attendance list
    period_attendance = {}
    for student in students:
        if action == "Mark All Present":
            period_attendance[student] = "Present"
        elif action == "Mark All Absent":
            period_attendance[student] = "Absent"
        else:
            status = st.radio(
                f"{student}", ["Present", "Absent", "No Class"],
                key=f"{student}_p{period}", horizontal=True)
            period_attendance[student] = status

    # Save entries for this period
    for student, status in period_attendance.items():
        all_entries.append({
            "Date": selected_date,
            "Period": period,
            "Teacher": teacher,
            "Student Name": student,
            "Status": status
        })

# Save data
if st.button("💾 Save Attendance"):
    df_new = pd.DataFrame(all_entries)

    if os.path.exists(xlsx_path):
        try:
            existing = pd.read_excel(xlsx_path)
            df_combined = pd.concat([existing, df_new], ignore_index=True)
        except:
            df_combined = df_new
    else:
        df_combined = df_new

    df_combined.to_excel(xlsx_path, index=False)
    st.success("✅ Attendance saved successfully to diary.xlsx")
