from shared_modules.database_interface import *
from models.replacement_number_map import ReplacementNumberMap
from shared_modules.logger import trace_logging


@trace_logging()
def get_replacement_map_item_with_number_to_replace(number_to_replace: str):

    sql = "SELECT * FROM replacementnumbermap WHERE replacementphonenumber = '" + number_to_replace + "'"
    my_result = DatabaseInterface().select(sql)
    if len(my_result) > 0:
        return ReplacementNumberMap(my_result[0])
    else:
        return None


@trace_logging()
def insert_replacement_map(replacement_map: ReplacementNumberMap):
    sql = "INSERT INTO replacementnumbermap ( replacementphonenumber, routingnumber, poolid ) " \
          "VALUES ( '" + replacement_map.replacementphonenumber + "', '" + replacement_map.routingnumber + "', '" + replacement_map.poolid + "' );"

    return DatabaseInterface().insert(sql)
