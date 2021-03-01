from SharedModules.DatabaseInterface import *
import Models.ReplacementNumberMap as map


def get_replacement_map_item_with_number_to_replace(number_to_replace: str):

    sql = "SELECT * FROM replacementnumbermap WHERE replacementphonenumber = '" + number_to_replace + "'"
    my_result = DatabaseInterface().select(sql)
    new_map = map.ReplacementNumberMap(my_result[0])

    return new_map

get_replacement_map_item_with_number_to_replace('234-123-4323')