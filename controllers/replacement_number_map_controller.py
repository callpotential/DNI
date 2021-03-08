from shared_modules.database_interface import *
from models.replacement_number_map import replacement_number_map
from shared_modules.logger import trace_logging


@trace_logging()
def get_replacement_map_item_with_number_to_replace(number_to_replace: str):

    sql = "SELECT * FROM replacementnumbermap WHERE replacementphonenumber = '" + number_to_replace + "'"
    my_result = database_interface().select(sql)
    new_map = replacement_number_map(my_result[0])

    return new_map
