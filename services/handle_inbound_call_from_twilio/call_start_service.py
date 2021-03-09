from twilio.twiml.voice_response import VoiceResponse

from controllers.session_information_log_controller import get_routing_number_from_pool_number
from shared_modules.logger import get_logger


def handler(event, context):
    get_logger().log_handler_enter(event, context)

    # Phone number that was called
    to = event['to']
    if to is None:
        return None

    routing_phone = get_routing_number_from_pool_number(to)
    if routing_phone is False:
        return None

    resp = VoiceResponse()
    resp.dial(routing_phone)

    get_logger().log_handler_exit(str(resp))
    return str(resp)
