# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say

response = VoiceResponse()
response.say('Nalehavost 2, BEZVĚDOMÍ, MUŽ 28 LET, Na Strážišti 1888, First Responder, na cestě RZP Kadaň.')

print(response)


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC6e61fea6d3796ce5cb6a1bd4b38aa95a'
auth_token = '1ae38b3f834a2759bbb0e0d13fa055da'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<?xml version="1.0" encoding="UTF-8"?><Response><Play>https://hasici.hrabova.net/wp-content/uploads/2015/12/20110403195720.wav</Play></Response>',
                        to='+420608834833',
                        from_='+420910880185'
                    )

print(call.sid)