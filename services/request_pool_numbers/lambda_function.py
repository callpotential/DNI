from services.request_pool_numbers.request_pool_numbers import request_pool_number
from shared_modules.lambda_helpers import rest_response, rest_success_response


def lambda_handler(event, context):
    try:
        if event['pool_size'] is None:
            return rest_response(400, "No 'pool_size' parameter specified")

        if event['area_code'] is None:
            return rest_response(400, "No 'area_code' parameter specified")

        if event['locality'] is None:
            return rest_response(400, "No 'locality' parameter specified")

        avail_phone_nums = request_pool_number(int(event['pool_size']), event['area_code'], event['locality'])

        return rest_success_response(avail_phone_nums)
    except Exception as e:
        return rest_response(500, str(e))
