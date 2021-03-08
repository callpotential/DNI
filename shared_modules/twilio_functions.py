from twilio.rest import Client

ACCOUNT_SID = "AC99cc9b8bf49b325289f896b2bb86c7d6"
ACCOUNT_TOKEN = "5793770e800dea86597819a14b53d63c"

def get_list_of_numbers_from_area_code(client, limit, area_code, locality):
    available_phone_number_country = None

    if area_code is None and locality is None:
        available_phone_number_country = client.available_phone_numbers('US').local.list(limit=limit, area_code=area_code, in_locality=locality)
    elif area_code is not None and locality is not None:
        available_phone_number_country = client.available_phone_numbers('US').local.list(limit=limit, area_code=area_code, in_locality=locality)
    elif area_code is not None and locality is None:
        available_phone_number_country = client.available_phone_numbers('US').local.list(limit=limit, area_code=area_code)
    elif area_code is None and locality is not None:
        available_phone_number_country = client.available_phone_numbers('US').local.list(limit=limit, in_locality=locality)

    list_of_number = []
    for item in available_phone_number_country:
        list_of_number.append(item.phone_number)

    return list_of_number

client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
# print(get_list_of_numbers_from_area_code(client, 2, 563, 'Chicago'))
# print(get_list_of_numbers_from_area_code(client, 2, 563, None))
# print(get_list_of_numbers_from_area_code(client, 2, None, 'Chicago'))
# print(get_list_of_numbers_from_area_code(client, 2, None, None))

def create_new_phone_number(client, phone_number):

    voice_url = "http://7229cde20d08.ngrok.io/answer?phone={0}".format(phone_number)
    status_url = "http://7229cde20d08.ngrok.io/end"

    incoming_phone_number = client.incoming_phone_numbers.create(phone_number=str(phone_number),voice_url=voice_url,status_callback=status_url)
    phone_number = incoming_phone_number.phone_number

number = get_list_of_numbers_from_area_code(client, 2, 563, 'Chicago')[0]
print(number)
create_new_phone_number(client, number)
