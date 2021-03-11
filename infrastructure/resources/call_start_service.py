from twilio.twiml.voice_response import VoiceResponse


def handler(event, context):
    resp = VoiceResponse()
    resp.say("Some stuff " + str(event['from']))
    return str(resp)
