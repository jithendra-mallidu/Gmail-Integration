import imaplib
import email
from twilio.rest import Client

# Function to read emails from Gmail

def read_gmail(user, password):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(user, password)
    mail.select('inbox')
    status, messages = mail.search(None, 'ALL')
    email_ids = messages[0].split()
    emails = []
    for email_id in email_ids[-5:]:  # get latest 5 emails
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        emails.append(msg)
    return emails

# Function to send WhatsApp notifications

def send_whatsapp_notification(to, body):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Change to your Twilio WhatsApp number
        body=body,
        to=f'whatsapp:{to}'
    )
    return message.sid

# Main function orchestrating the workflow

def main():
    user = 'your_email@gmail.com'
    password = 'your_password'
    whatsapp_number = 'whatsapp_recipient_number'

    emails = read_gmail(user, password)
    for email in emails:
        subject = email['subject']
        body = email.get_payload(decode=True).decode()  # Decode email body
        notification_msg = f'Subject: {subject}\nBody: {body}'
        send_whatsapp_notification(whatsapp_number, notification_msg)

if __name__ == '__main__':
    main()