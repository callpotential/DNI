import json
from services.number_assignment.number_assignment_service import number_assignment_get_number
from shared_modules.lambda_helpers import rest_response, rest_success_response


def lambda_handler(event, context):
    if event['url'] is None:
        return rest_response(400, "No 'url' parameter specified")

    if event['phone'] is None:
        return rest_response(400, "No 'phone' parameter specified")

    resp = number_assignment_get_number(event['url'], event['phone'])

    # TODO implement
    return rest_success_response()
