from flask import Flask
from flask import request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)
ACCOUNT_SID = "AC99cc9b8bf49b325289f896b2bb86c7d6"
ACCOUNT_TOKEN = "5793770e800dea86597819a14b53d63c"

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # sid = request.args.get('sid')
    # print(sid)
    phone = request.args.get('phone')
    print(phone)

    # Read a message aloud to the caller
    resp.say("Thank you for calling! Have a great day.", voice='alice')

    return str(resp)

@app.route("/end", methods=['GET', 'POST'])
def end_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    print("call is over")
    # Read a message aloud to the caller

    resp = VoiceResponse()
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)
