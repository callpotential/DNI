from SharedModules.DatabaseInterface import *
from Models.ReplacementNumberMap import ReplacementNumberMap


def get_replacement_map_item_with_number_to_replace(number_to_replace: str):

    sql = "SELECT * FROM replacementnumbermap WHERE replacementphonenumber = '" + number_to_replace + "'"
    my_result = DatabaseInterface().select(sql)
    new_map = ReplacementNumberMap(my_result[0])

    return new_map
