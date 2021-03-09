from twilio.twiml.voice_response import VoiceResponse

from controllers.assignment_pool_controller import set_ttl_expiry
from controllers.session_information_log_controller import get_session_item_with_pool_number
from shared_modules.logger import get_logger


def transmit_to_cp_call_log():
    pass


def handler(event, context):
    get_logger().log_handler_enter(event, context)

    # Phone number that was called
    to = event['to']
    if to is None:
        return None

    set_ttl_expiry(to)
    session_item = get_session_item_with_pool_number(to)
    if session_item.clickid:
        transmit_to_cp_call_log()

    resp = VoiceResponse()
    get_logger().log_handler_exit(str(resp))
    return resp
