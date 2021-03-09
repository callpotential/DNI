from twilio.rest import Client

ACCOUNT_SID = "AC99cc9b8bf49b325289f896b2bb86c7d6"
ACCOUNT_TOKEN = "5793770e800dea86597819a14b53d63c"


class PhoneNumberService:

    def __init__(self, sid: str = ACCOUNT_SID, token: str = ACCOUNT_TOKEN):
        self.client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
        self.call_receive_url = ""
        self.call_end_url = ""

    def call_receive_webhook(self, url):
        self.call_receive_url = url

    def call_end_webhook(self, url):
        self.call_end_url = url

    def list_available_phone_numbers(self, limit: int, area_code: str = None, locality: str = None) -> [str]:
        available_phone_number_country = None
        if area_code is None and locality is None:
            available_phone_number_country = self.client.available_phone_numbers('US').local.list(limit=limit)
        elif area_code is not None and locality is not None:
            available_phone_number_country = self.client.available_phone_numbers('US').local.list(limit=limit, area_code=area_code, in_locality=locality)
        elif area_code is not None and locality is None:
            available_phone_number_country = self.client.available_phone_numbers('US').local.list(limit=limit, area_code=area_code)
        elif area_code is None and locality is not None:
            available_phone_number_country = self.client.available_phone_numbers('US').local.list(limit=limit, in_locality=locality)

        list_of_number = []
        for item in available_phone_number_country:
            list_of_number.append(item.phone_number)

        return list_of_number

    # TODO ASH Figure out what is returned when the number is not properly provisioned
    def create_new_phone_number(self, phone_number: str):
        self.client.incoming_phone_numbers.create(phone_number=phone_number, voice_url=self.call_receive_url, status_callback=self.call_end_url)
