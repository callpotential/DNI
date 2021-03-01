from SharedModules.DatabaseInterface import *
import Models.SessionInformationLog as session

def get_session_item_with_click_id(clickid:str):
    """DB Interface
    This function will reach out to the database and get a session item using the click id.
    """

    sql = "SELECT * FROM SessionInformationLog WHERE clickid = '" + clickid + "'"

    my_result = DatabaseInterface.get_database().select(sql)

    if my_result:
        session_item = session.SessionInformationLog(my_result[0])
        return session_item
    else:
        return False