# twilio-custom-msg

### Setup
1. Create a twilio account, and buy a phone number.
2. Retrieve Account SSID, Auth Token, and phone number.
3. Clone or unzip this repository.
4. Set up virtual enviroment, and activate.
5. install twilio api, with ``pip install twilio``


### Configuring
You can configure your credentials by setting up your enviroment variables like:
```
export TWILIO_ACCOUNT_SID='Your Twilio Account SID'
export TWILIO_AUTH_TOKEN='Your Twilio Auth Token'
export TWILIO_PHONE_NUMBER='Your Twilio Phone Number'
```
or setting enter into the strings like:
```
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID") if os.environ.get("TWILIO_ACCOUNT_SID") else 'Your Twilio Account SID'
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN") if os.environ.get("TWILIO_AUTH_TOKEN") else 'Your Twilio Auth Token'
FROM_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER") if os.environ.get("TWILIO_PHONE_NUMBER") else 'your Twilio Phone Number'
```
### Building
1. Activate virtual enviroment.
2. execute executable.
