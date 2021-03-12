from services.request_pool_numbers.request_pool_numbers import request_pool_number
from shared_modules.lambda_helpers import rest_response, rest_success_response
from shared_modules.logger import trace_logging


@trace_logging()
def lambda_handler(event, context):
    try:
        if 'pool_size' not in event:
            return rest_response(400, "No 'pool_size' parameter specified")

        if 'area_code' not in event:
            event['area_code'] = None

        if 'locality' not in event:
            event['locality'] = None

        avail_phone_nums = request_pool_number(int(event['pool_size']), event['area_code'], event['locality'])

        return rest_success_response(avail_phone_nums)
    except Exception as e:
        return rest_response(500, str(e))
