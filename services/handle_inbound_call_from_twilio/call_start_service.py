from twilio.twiml.voice_response import VoiceResponse
from controllers.session_information_log_controller import get_routing_number_from_pool_number
from models.phone_number import PhoneNumber
from shared_modules.logger import trace_logging


@trace_logging()
def call_start_service(called_number: PhoneNumber):
    routing_phone = get_routing_number_from_pool_number(called_number)
    if routing_phone is None:
        return None

    resp = VoiceResponse()
    resp.dial(routing_phone)
    return str(resp)
