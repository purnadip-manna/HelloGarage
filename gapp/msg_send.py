from twilio.rest import Client
import os

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']


client = Client(account_sid, auth_token)

def sendmsg(otp, phnno, state):
    message = client.messages.create(
        from_='+18176318562',
        body='<#> Your OTP is ' + str(otp) + ' for '+ state +'. Thank You - Hello Garage!',
        to="+91"+str(phnno)
    )

    print(message.sid)