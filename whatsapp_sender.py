import os
from twilio.rest import Client

# Twilio credentials
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
from_number = os.environ.get('TWILIO_FROM_NUMBER')

# Function to send WhatsApp message
def send_whatsapp_message(to_number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_='whatsapp:' + from_number,
        to='whatsapp:' + to_number
    )
    return message.sid

# Example usage
if __name__ == '__main__':
    recipient_number = '+1234567890'  # Replace with recipient's WhatsApp number
    spending_summary = 'Here is your spending summary for the week.'  # Summarize spending details
    send_whatsapp_message(recipient_number, spending_summary)
