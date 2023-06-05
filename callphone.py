# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 10:37:02 2022

@author: mustafa
"""
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

account_sid = "AC51efada95ce35755e082da272319bc57"
auth_token  = "79d43ca966d77cfd18ae92411efda118"

client = Client(account_sid, auth_token)

twiml = VoiceResponse()
#twiml.say('Hello, from Python!')

call = client.calls.create(
    from_='+13252412522',
    to='+905059400196',
    twiml=str(twiml),
)
