from models.phone_number import PhoneNumber
from services.number_assignment.number_assignment_service import get_assignment_pool_number
from shared_modules.lambda_helpers import rest_response, rest_success_response


def lambda_handler(event, context):
    try:
        if event['url'] is None:
            return rest_response(400, "No 'url' parameter specified")

        if event['phone'] is None:
            return rest_response(400, "No 'phone' parameter specified")

        resp = get_assignment_pool_number(event['url'], PhoneNumber(event['phone']))

        return rest_success_response(resp)
    except Exception as e:
        return rest_response(500, str(e))
