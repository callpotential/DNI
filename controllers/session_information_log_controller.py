from models.phone_number import PhoneNumber
from shared_modules.database_interface import *
from models.session_information_log import SessionInformationLog
from shared_modules.logger import trace_logging
import datetime

from shared_modules.proxy_date_time import ProxyDateTime


@trace_logging()
def get_session_item_with_click_id(clickid: str):
    """DB Interface
    This function will reach out to the database and get a session item using the click id.
    """

    sql = "SELECT * FROM sessioninformationlog WHERE clickid = '" + str(clickid) + "'"

    my_result = DatabaseInterface().select(sql)
    if len(my_result) > 0:
        return SessionInformationLog(my_result[0])
    else:
        return None


@trace_logging()
def get_session_item_with_pool_number(pool_number: PhoneNumber):
    sql = "SELECT * FROM sessioninformationlog WHERE poolphonenumber = '" + str(pool_number) + "'"
    my_result = DatabaseInterface().select(sql)

    if len(my_result) > 0:
        return SessionInformationLog(my_result[0])
    else:
        return None


@trace_logging()
def get_routing_number_from_pool_number(pool_number: PhoneNumber):
    session_item = get_session_item_with_pool_number(pool_number)
    if session_item is None:
        return None
    else:
        return session_item.routingnumber.get_with_dashes()


@trace_logging()
def create_new_session_item(session_object_dict):
    session_item = SessionInformationLog(session_object_dict)

    session_dict = session_item.__dict__
    session_dict.pop("sessionid")

    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in session_dict.keys())
    values = ', '.join(values_handler(x) for x in session_dict.values())
    sql = "INSERT INTO sessioninformationlog ( %s ) VALUES ( %s );" % (columns, values)

    session_item.sessionid = DatabaseInterface().insert(sql)

    return session_item


@trace_logging()
def update_call_start(pool_number: PhoneNumber, time: datetime = ProxyDateTime.now()):
    sql = ("UPDATE sessioninformationlog SET callstart = '" + str(ProxyDateTime.date_time_to_sql(time)) + "' WHERE poolphonenumber = '" + str(pool_number) + "'")
    DatabaseInterface().update(sql)


@trace_logging()
def update_call_end(pool_number: PhoneNumber, time: datetime = ProxyDateTime.now()):
    sql = ("UPDATE sessioninformationlog SET callend = '" + str(ProxyDateTime.date_time_to_sql(time)) + "' WHERE poolphonenumber = '" + str(pool_number) + "'")
    DatabaseInterface().update(sql)


@trace_logging()
def values_handler(x):
    if type(x) == str:
        return "'" + x.replace('/', '_') + "'"
    elif type(x) == int:
        return str(x)
    elif type(x) == datetime.datetime:
        return "'" + str(x) + "'"
    else:
        return str(x)
