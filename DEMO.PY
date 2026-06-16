import streamlit as st
st.title("REGISTRATION FORM")
name=st.text_input("Enter your name")
email=st.text_input("Enter your email")
age=st.number_input("Enter your age", min_value=1, max_value=100)
gender=st.radio("Select Gender",["Male","Female","Other"],index=None)
course=st.selectbox("select course:",["Python","Java","C++","JavaScript"],index=None)
if st.button ("registration"):
    if name and email:
      st.success("registration successful")
      st.write("Your details:")   
      st.write(f"Name: {name}")
      st.write(f"Email: {email}")
      st.write(f"Age: {age}")
      st.write(f"Gender: {gender}")
      st.write(f"Course: {course}")
    else:
      st.error("fill all blanks")











