
import streamlit as st
import pandas as pd
from datetime import date
import os

# Path to the Excel file
xls_path = "diary.xlsx"

# Student list
students = [
    "Abhirami.K.P", "Aiswarya P.S", "Amritha Balakrishnan", "Ardra Suresh.M",
    "Asmin M.A", "Athira P.P", "Bismi Thomas", "Divya R.Prabhu",
    "Gokuldas. O.H", "Hajarabi C.M", "Harikrishnan E.M", "Krishna Priya P.S"
]

st.title("📋 Daily Attendance Recorder")
today = date.today()

# Select date
selected_date = st.date_input("Select Date", value=today)

# Mark attendance
st.subheader("Mark Present Students:")
present_students = st.multiselect("Select students who are present today:", students)

if st.button("✅ Submit Attendance"):
    # Prepare today's attendance
    records = []
    for s in students:
        status = "Present" if s in present_students else "Absent"
        records.append({"Date": selected_date, "Student Name": s, "Status": status})
    df_new = pd.DataFrame(records)

    # Append to existing file or create new
    if os.path.exists(xls_path):
        try:
            existing = pd.read_excel(xls_path)
            df_final = pd.concat([existing, df_new], ignore_index=True)
        except:
            df_final = df_new
    else:
        df_final = df_new

    # Save updated file
    df_final.to_excel(xls_path, index=False)
    st.success(f"✅ Attendance for {selected_date} saved successfully!")
