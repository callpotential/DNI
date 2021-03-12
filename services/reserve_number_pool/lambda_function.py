import json
from models.phone_number import PhoneNumber
from services.reserve_number_pool.reserve_number_pool import reserve_number_pool
from shared_modules.lambda_helpers import rest_response, rest_success_response
from shared_modules.logger import trace_logging


@trace_logging()
def lambda_handler(event, context):
    try:
        if 'replace_num' not in event:
            return rest_response(400, "No 'replace_num' parameter specified")

        if 'routing_num' not in event:
            return rest_response(400, "No 'routing_num' parameter specified")

        if 'business_id' not in event:
            return rest_response(400, "No 'business_id' parameter specified")

        if 'requested_numbers' not in event:
            return rest_response(400, "No 'requested_numbers' parameter specified")

        # Default to 1 if not supplied for now
        if 'pool_id' not in event:
            event['pool_id'] = 1

        reserve_number_pool(PhoneNumber(event['replace_num']), PhoneNumber(event['routing_num']), int(event['business_id']), json.loads(event['requested_numbers']), event['pool_id'])

        return rest_success_response()
    except Exception as e:
        return rest_response(500, str(e))
