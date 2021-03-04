from flask import Flask
from flask import request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import json
import urllib.request

app = Flask(__name__)
ACCOUNT_SID = "AC99cc9b8bf49b325289f896b2bb86c7d6"
ACCOUNT_TOKEN = "5793770e800dea86597819a14b53d63c"

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    sid = request.args.get('sid')
    print(sid)
    phone = request.args.get('phone')
    print(phone)

    client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)

    incoming_phone_number = client.incoming_phone_numbers.create(phone_number=str('+' + str(phone)))
    print(incoming_phone_number.date_created)

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

def get_list_of_numbers_from_area_code(client, limit, area_code, locality):
    available_phone_number_country = None

    if area_code == None and locality == None:
        available_phone_number_country = client.available_phone_numbers('US').local.list(limit=limit, area_code=area_code, in_locality=locality)
    elif area_code != None and locality != None:
        available_phone_number_country = client.available_phone_numbers('US').local.list(limit=limit, area_code=area_code, in_locality=locality)
    elif area_code != None and locality == None:
        available_phone_number_country = client.available_phone_numbers('US').local.list(limit=limit, area_code=area_code)
    elif area_code == None and locality != None:
        available_phone_number_country = client.available_phone_numbers('US').local.list(limit=limit, in_locality=locality)

    list_of_number = []
    for item in available_phone_number_country:
        list_of_number.append(item.phone_number)

    return list_of_number

client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
print(get_list_of_numbers_from_area_code(client, 2, 563, 'Chicago'))
print(get_list_of_numbers_from_area_code(client, 2, 563, None))
print(get_list_of_numbers_from_area_code(client, 2, None, 'Chicago'))
print(get_list_of_numbers_from_area_code(client, 2, None, None))

def number_hook():
    client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)

    available_phone_number_country = client.available_phone_numbers('US').local.list(area_code=563,limit=200,in_locality='Chicago')

    list_of_number = []
    for item in available_phone_number_country:
        list_of_number.append(item.phone_number)
    print(list_of_number)

    # fileurl = 'https://api.twilio.com/' + str(available_phone_number_country.subresource_uris['local'])
    # numbers = client.available_phone_numbers.get_page(fileurl)
    # numbers_dict = numbers.__dict__
    #
    # pass_numbers = []
    # for item in numbers_dict['_payload']['available_phone_numbers']:
    #     if item['phone_number'].startswith('+1312'):
    #         pass_numbers.append(item)
    #
    # print(pass_numbers)

    # with urllib.request.urlopen() as f:
    #     data = json.load(f)

    # incoming_phone_number = client.
    # call = client.incoming_phone_numbers.create()

if __name__ == "__main__":
    app.run(debug=True)





