import streamlit as st
import datetime
time = datetime.datetime.now()
st.title("Automating your Whatsapp Message")
import pywhatkit as py
phonelist = st.text_input("Please input numbers you want to automate with seperated by ,")
message = st.text_area("Enter your Message")
submit = st.button("Enter")
i=1
if submit:
    phone = phonelist.split(',')
    for each in phone:
        py.sendwhatmsg("+91"+each,message,time.hour,(time.minute+i))
        i=i+2
    st.success("Message Send!")
