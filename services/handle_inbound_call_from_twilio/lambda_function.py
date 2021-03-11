from services.handle_inbound_call_from_twilio.call_start_service import call_start_service
from shared_modules.lambda_helpers import json_to_xml
from shared_modules.logger import trace_logging


# Because this is a twilio handler this must return a xml response
@trace_logging()
def lambda_handler(event, context):
    if event['to'] is None:
        return json_to_xml("No 'to' parameter specified")

    resp = call_start_service(event['to'])
    return json_to_xml(str(resp))
