from twilio.rest import Client

account_sid = 'AC4fc7157a3b90b69a2d1dbc37ca1b4d4d'
auth_token = '848deda749f8c8d3829486ead41f142b'

client = Client(account_sid, auth_token)

def sendmsg(otp, phnno, state):
    message = client.messages.create(
        from_='+18176318562',
        body='<#> Your OTP is ' + str(otp) + ' for '+ state +'. Thank You - Hello Garage!',
        to="+91"+str(phnno)
    )

    print(message.sid)