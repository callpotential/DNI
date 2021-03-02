from SharedModules.DatabaseInterface import *
import Models.SessionInformationLog as session
from Models.SessionInformationLog import SessionInformationLog

def get_session_item_with_click_id(clickid:str):
    """DB Interface
    This function will reach out to the database and get a session item using the click id.
    """

    sql = "SELECT * FROM SessionInformationLog WHERE clickid = '" + clickid + "'"

    my_result = DatabaseInterface().select(sql)

    if my_result:
        session_item = SessionInformationLog(my_result[0])
        return session_item
    else:
        return False

