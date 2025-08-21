import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from tools.formatter import format_text_local

load_dotenv()

def send_email(raw_message: str, subject: str, receiver_emails: list[str]):
    
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_APP_PASSWORD")

    if not sender_email or not sender_password:
        raise ValueError("SENDER_EMAIL or SENDER_APP_PASSWORD not found in environment variables.")

    formatted_message = format_text_local(raw_message, mode="email")

    msg = MIMEText(formatted_message)
    msg["Subject"] = subject
    msg["From"] = sender_email

    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_emails, msg.as_string())
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Error sending email: {str(e)}"
