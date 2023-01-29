#Importing the library os for miscellaneous operating system interfaces
import os
from twilio.rest import Client

# Setting environment variables for a user credentials in case of emmergency
account_sid = "ACcbad5be15323b5850ecd954c7a286689"
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

# Creating a demo call to reach out a specific number for emergency
call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  
# For demo purposes I've used my personal number, but this number will be replaced by emergency contact like "911" so the bike riders can get help just in case a accident actually happens. 
  to="+12673618594",
  
  from_="+18337051333"
)

print(call.sid)