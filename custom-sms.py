from twilio.rest import Client
import os

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID") if os.environ.get("TWILIO_ACCOUNT_SID") else ''
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN") if os.environ.get("TWILIO_AUTH_TOKEN") else ''
FROM_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER") if os.environ.get("TWILIO_PHONE_NUMBER") else ''

phone = input('Phone number: ')
msg = input('Message: ')
print()
print('Phone: ' + phone)
print('Message: ' + msg)
if input('is this correct? ') == 'yes':
	client = Client(ACCOUNT_SID, AUTH_TOKEN)
	client.messages.create(
		to=phone,
		from_=FROM_NUMBER,
		body=msg
	)