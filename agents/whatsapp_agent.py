import os
from dotenv import load_dotenv
from twilio.rest import Client
from tools.formatter import format_text_local

load_dotenv()

def send_whatsapp_message(raw_message: str, receiver_numbers: list[str]):
    
    twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_sender = os.getenv("TWILIO_WHATSAPP_NUMBER")

    if not (twilio_sid and twilio_auth and twilio_sender):
        raise ValueError("Twilio credentials not found in environment variables (.env).")

    formatted_text = format_text_local(raw_message, mode="whatsapp")

    client = Client(twilio_sid, twilio_auth)
    responses = []

    for num in receiver_numbers:
        try:
            result = client.messages.create(
                body=formatted_text,
                from_=twilio_sender,        
                to=f"whatsapp:{num}"        
            )
            responses.append(f"Message Send Successfully")
        except Exception as e:
            responses.append(f"Error sending to {num}: {str(e)}")

    return responses
