from twilio.rest import TwilioRestClient

account_sid = "AC703e6c9fd4185ff7d9b6d2097b7640c2" # Your Account SID from www.twilio.com/console
auth_token  = "5fef5b6107fc8e14d1f1292833075f16"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello my name is harshit",
    to="+919897674175",    # Replace with your phone number
    from_="+919458815360") # Replace with your Twilio number

print(message.sid)
