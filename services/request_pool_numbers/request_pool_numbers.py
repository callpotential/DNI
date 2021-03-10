from shared_modules.logger import get_logger
from shared_modules.twilio_functions import PhoneNumberService


def handler(event, context):
    get_logger().log_handler_enter(event, context)

    pool_size = event['pool_size']
    area_code = event['area_code']
    locality = event['locality']

    service = PhoneNumberService()
    avail_phone_nums = service.list_available_phone_numbers(pool_size, area_code, locality)

    resp = avail_phone_nums
    get_logger().log_handler_exit(resp)
    return resp
