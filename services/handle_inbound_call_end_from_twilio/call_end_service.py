from controllers.assignment_pool_controller import set_ttl_expiry
from controllers.session_information_log_controller import get_session_item_with_pool_number, update_call_end
from models.phone_number import PhoneNumber
from shared_modules.logger import trace_logging


@trace_logging()
def transmit_to_cp_call_log():
    pass


@trace_logging()
def call_end_service(called_number: PhoneNumber):
    update_call_end(called_number)
    set_ttl_expiry(called_number)
    session_item = get_session_item_with_pool_number(called_number)
    if session_item.clickid:
        transmit_to_cp_call_log()
