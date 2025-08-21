import streamlit as st
from agents.email_agent import send_email
from agents.whatsapp_agent import send_whatsapp_message

st.set_page_config(page_title="Messaging Agent", layout="centered")

st.title(" Messaging Agent (Email + WhatsApp)")

message = st.text_area("Enter the message:", height=150)

tab1, tab2 = st.tabs(["Email Agent", "WhatsApp Agent"])

with tab1:
    st.subheader("Email Sender Options")
    subject = st.text_input("Email Subject", "")
    email_receivers = st.text_input("Receiver Emails (comma separated)")
    
    if st.button("Send Email"):
        if not (message and subject and email_receivers):
            st.warning("Please fill message, subject, and emails.")
        else:
            receiver_list = [e.strip() for e in email_receivers.split(",")]
            result = send_email(message, subject, receiver_list)
            st.success(result)

with tab2:
    st.subheader("WhatsApp Sender Options")
    whatsapp_receivers = st.text_input("Receiver WhatsApp Numbers (comma separated, +91...)")
    
    if st.button("Send WhatsApp"):
        if not (message and whatsapp_receivers):
            st.warning("Please fill message and WhatsApp numbers.")
        else:
            number_list = [n.strip() for n in whatsapp_receivers.split(",")]
            result_list = send_whatsapp_message(message, number_list)
            for res in result_list:
                st.write(res)