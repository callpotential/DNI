from shared_modules.database_interface import *
import models.session_information_log as session
from models.session_information_log import SessionInformationLog
from shared_modules.logger import trace_logging


@trace_logging()
def get_session_item_with_click_id(clickid:str):
    """DB Interface
    This function will reach out to the database and get a session item using the click id.
    """

    sql = "SELECT * FROM session_information_log WHERE clickid = '" + clickid + "'"

    my_result = DatabaseInterface().select(sql)

    if my_result:
        session_item = SessionInformationLog(my_result[0])
        return session_item
    return False


@trace_logging()
def get_session_item_with_pool_number(pool_number: str):
    sql = "SELECT * FROM session_information_log WHERE poolphonenumber = '" + pool_number + "'"
    my_result = DatabaseInterface().select(sql)

    if len(my_result) > 0:
        return SessionInformationLog(my_result[0])
    else:
        return False


@trace_logging()
def get_routing_number_from_pool_number(pool_number: str):
    session_item = get_session_item_with_pool_number(pool_number)
    if session_item is False:
        return False
    else:
        return session_item.routingnumber


@trace_logging()
def create_new_session_item(session_object_dict):
    session_item = SessionInformationLog(session_object_dict)

    session_dict = session_item.__dict__
    session_dict.pop("sessionid")

    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in session_dict.keys())
    values = ', '.join(values_handler(x) for x in session_dict.values())
    sql = "INSERT INTO session_information_log ( %s ) VALUES ( %s );" % (columns, values)

    id = DatabaseInterface().insert(sql)
    session_item.sessionid = id

    return session_item

@trace_logging()
def values_handler(x):
    if type(x) == str:
        return "'" + x.replace('/', '_') + "'"
    elif type(x) == int:
        return str(x)
    else:
        return str(x)
