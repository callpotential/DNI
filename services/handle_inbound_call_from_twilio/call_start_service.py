from twilio.twiml.voice_response import VoiceResponse

from controllers.assignment_pool_controller import get_session_id_from_pool_number
from controllers.session_information_log_controller import get_routing_number_from_pool_number, update_call_start
from models.phone_number import PhoneNumber
from shared_modules.logger import trace_logging


@trace_logging()
def call_start_service(called_number: PhoneNumber):
    session_id = get_session_id_from_pool_number(called_number)
    if session_id is None:
        return None

    update_call_start(session_id)

    # Call forwarding
    routing_phone = get_routing_number_from_pool_number(called_number)
    if routing_phone is None:
        return None

    resp = VoiceResponse()
    resp.dial(str(routing_phone))
    return str(resp)
