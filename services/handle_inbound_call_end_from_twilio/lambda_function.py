from models.phone_number import PhoneNumber
from services.handle_inbound_call_end_from_twilio.call_end_service import call_end_service
from shared_modules.lambda_helpers import rest_response, rest_success_response
from shared_modules.logger import trace_logging


@trace_logging()
def lambda_handler(event, context):
    try:
        if 'Called' not in event:
            return rest_response(400, "No 'Called' parameter specified")

        call_end_service(PhoneNumber(event['Called']))

        return rest_success_response()
    except Exception as e:
        return rest_response(500, str(e))
