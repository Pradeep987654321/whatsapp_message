import streamlit as st
import pywhatkit
import time  # For adding a delay


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


# Streamlit app title
st.title("Scheduled WhatsApp Message Sender")

# Input fields
phone_number = st.text_input("Enter Your Phone Number with Country Code (e.g., +1234567890)")
message = st.text_area("Enter Your Message")
schedule_hour = st.number_input("Enter Your Schedule Hour (24-hour format)", min_value=0, max_value=23, step=1)
schedule_minute = st.number_input("Enter Your Schedule Minute", min_value=0, max_value=59, step=1)

# Button to trigger the sending process
if st.button("Send Message"):
    if phone_number and message:
        try:
            st.info("Preparing to send the message...")
            time.sleep(2)  # Add a small delay

            # Send the WhatsApp message at the scheduled time
            pywhatkit.sendwhatmsg(phone_number, message, schedule_hour, schedule_minute)
            
            st.success(f"Message scheduled successfully to {phone_number} at {schedule_hour:02d}:{schedule_minute:02d}!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill out all fields.")
