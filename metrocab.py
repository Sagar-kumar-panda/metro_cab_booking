import streamlit as st
st.title("METRO + CAB BOOKING")
#METRO STATION LIST
stations=[
    "SELECT",
    "MIYAPUR",
    "JNTUH",
    "NAGOLE",
    "AMEERPET",
    "LB NAGAR",
    "DILSUKNAGAR"
]
from_station=st.selectbox("FROM",stations,index=None)
to_station=st.selectbox("TO",stations,index=None)
tickets=st.number_input("TICKETS", min_value=1, max_value=10)
need_cab=st.radio("do you need a cab?",["yes","no"],index=None)
cab_fare=0
if (need_cab=="yes"):
    cab_destination=st.text_input("Enter destination:")

    cab_fare=130
if st.button("book"):
    if from_station == to_station:
        st.error("FROM and TO stations cannot be the same.")
    else:
        metro_fare=30 * tickets
        total=metro_fare + cab_fare
        st.success("Booking successful!")
        st.write(f"FROM: {from_station}")
        st.write(f"TO: {to_station}")
        st.write(f"TICKETS: {tickets}")
        st.write(f"metro_fare: {metro_fare}")
        if need_cab == "yes":
            st.write(f"cab from:{to_station}")
            st.write(f"to:{cab_destination}")
            st.write(f"cab bill:{cab_fare}")
            st.write(f"---total bill---:{total}")