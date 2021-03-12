from models.phone_number import PhoneNumber
from services.number_assignment.number_assignment_service import get_assignment_pool_number
from shared_modules.lambda_helpers import rest_response, rest_success_response
from shared_modules.logger import trace_logging


@trace_logging()
def lambda_handler(event, context):
    try:
        if 'url' not in event:
            return rest_response(400, "No 'url' parameter specified")

        if 'phone' not in event:
            return rest_response(400, "No 'phone' parameter specified")

        resp = get_assignment_pool_number(event['url'], PhoneNumber(event['phone']))

        response = dict()
        response['new_number'] = str(resp[0])
        response['message'] = str(resp[1])

        return rest_success_response(response)
    except Exception as e:
        return rest_response(500, str(e))
