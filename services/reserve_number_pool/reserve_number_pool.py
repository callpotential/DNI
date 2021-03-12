from controllers.assignment_pool_controller import register_assignment_pool_number
from controllers.replacement_number_map_controller import insert_replacement_map
from models.phone_number import PhoneNumber
from models.replacement_number_map import ReplacementNumberMap
from shared_modules.logger import trace_logging
from shared_modules.twilio_functions import PhoneNumberService


# TODO ASH business_id can be swapped to some other unique business identifier
@trace_logging()
def reserve_number_pool(replace_num: PhoneNumber, routing_num: PhoneNumber, business_id: int, requested_numbers: [str]):
    replacement_map = ReplacementNumberMap()
    replacement_map.replacementphonenumber = replace_num
    replacement_map.routingnumber = routing_num

    service = PhoneNumberService()
    for phone_number_str in requested_numbers:
        phone_number = PhoneNumber(phone_number_str)
        if service.create_new_phone_number(phone_number) is None:
            raise Exception('Error provisioning ' + str(phone_number))

        if register_assignment_pool_number(phone_number, replacement_map.routingnumber, business_id) is None:
            raise Exception('Error registering ' + str(phone_number))

        if insert_replacement_map(replacement_map) is None:
            raise Exception('Error registering replacement map for ' + str(phone_number))
