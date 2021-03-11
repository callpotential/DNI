from controllers.assignment_pool_controller import register_assignment_pool_number
from controllers.replacement_number_map_controller import insert_replacement_map
from models.phone_number import PhoneNumber
from models.replacement_number_map import ReplacementNumberMap
from shared_modules.logger import get_logger
from shared_modules.twilio_functions import PhoneNumberService


def handler(event, context):
    get_logger().log_handler_enter(event, context)

    replacement_map = ReplacementNumberMap()
    replacement_map.replacementphonenumber = event['replace_num']
    replacement_map.routingnumber = PhoneNumber(event['forward_num'])
    business_id: int = event['business_id']  # TODO ASH This can be swapped to some other unique business identifier
    requested_numbers: [str] = event['requested_numbers']

    service = PhoneNumberService()
    for phone_number_str in requested_numbers:
        if service.create_new_phone_number(PhoneNumber(phone_number_str)) is None:
            print('Error provisioning ' + phone_number_str)
            continue

        if register_assignment_pool_number(PhoneNumber(phone_number_str), replacement_map.routingnumber, business_id) is None:
            print('Error registering ' + phone_number_str)
            continue

        if insert_replacement_map(replacement_map) is None:
            print('Error registering replacement map for ' + phone_number_str)
            continue


    resp = None
    get_logger().log_handler_exit(resp)
    return resp