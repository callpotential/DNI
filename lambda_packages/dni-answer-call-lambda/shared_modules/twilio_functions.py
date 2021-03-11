from twilio.base import values
from twilio.rest import Client
from models.phone_number import PhoneNumber
from shared_modules.logger import trace_logging

ACCOUNT_SID = "AC99cc9b8bf49b325289f896b2bb86c7d6"
ACCOUNT_TOKEN = "5793770e800dea86597819a14b53d63c"
CALL_RECEIVE_URL = ''
CALL_END_URL = ''


class PhoneNumberService:

    # TODO ASH Turn this into a singleton or a factory, and convert these to environment variables
    def __init__(self, sid: str = ACCOUNT_SID, token: str = ACCOUNT_TOKEN, call_receive_url: str = CALL_RECEIVE_URL, call_end_url: str = CALL_END_URL):
        self.client = Client(sid, token)
        self.call_receive_url = call_receive_url
        self.call_end_url = call_end_url
        self.region = 'US'

    @trace_logging()
    def list_available_phone_numbers(self, limit: int, area_code: str = None, locality: str = None) -> [str]:
        # Convert to Twilio's version of unset values
        if area_code is None:
            area_code = values.unset
        if locality is None:
            locality = values.unset

        available_phone_number_country = self.client.available_phone_numbers(self.region).local.list(limit=limit, area_code=area_code, in_locality=locality)

        list_of_number = []
        for item in available_phone_number_country:
            list_of_number.append(item.phone_number)

        return list_of_number

    # TODO ASH Figure out what is returned when the number is not properly provisioned
    @trace_logging()
    def create_new_phone_number(self, phone_number: PhoneNumber):
        self.client.incoming_phone_numbers.create(phone_number=phone_number.get_twilio_format(), voice_url=self.call_receive_url, status_callback=self.call_end_url)