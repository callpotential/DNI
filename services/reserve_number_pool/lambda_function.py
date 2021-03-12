from models.phone_number import PhoneNumber
from services.reserve_number_pool.reserve_number_pool import reserve_number_pool
from shared_modules.lambda_helpers import rest_response, rest_success_response


def lambda_handler(event, context):
    try:
        if event['replace_num'] is None:
            return rest_response(400, "No 'replace_num' parameter specified")

        if event['routing_num'] is None:
            return rest_response(400, "No 'routing_num' parameter specified")

        if event['business_id'] is None:
            return rest_response(400, "No 'business_id' parameter specified")

        if event['requested_numbers'] is None:
            return rest_response(400, "No 'requested_numbers' parameter specified")

        reserve_number_pool(PhoneNumber(event['replace_num']), PhoneNumber(event['routing_num']), int(event['business_id']), event['requested_numbers'])

        return rest_success_response()
    except Exception as e:
        return rest_response(500, str(e))
