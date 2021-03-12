from shared_modules.logger import trace_logging
from shared_modules.twilio_functions import PhoneNumberService


@trace_logging()
def request_pool_number(pool_size: int, area_code: str, locality: str):
    service = PhoneNumberService()
    return service.list_available_phone_numbers(pool_size, area_code, locality)
