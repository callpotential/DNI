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

# def get_next_session_id():
#     sql = "SELECT * FROM SessionInformationLog WHERE max(sessionid)"
#     my_result = DatabaseInterface().select(sql)
#     print(my_result)


def create_new_session_item(session_object_dict):
    session_item = SessionInformationLog(session_object_dict)

    session_dict = session_item.__dict__
    session_dict.pop("sessionid")

    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in session_dict.keys())
    values = ', '.join(values_handler(x) for x in session_dict.values())
    sql = "INSERT INTO SessionInformationLog ( %s ) VALUES ( %s );" % (columns, values)

    id = DatabaseInterface().insert(sql)
    session_item.sessionid = id

    return session_item

def values_handler(x):
    if type(x) == str:
        return "'" + x.replace('/', '_') + "'"
    elif type(x) == int:
        return str(x)