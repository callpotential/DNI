from datetime import timedelta
from shared_modules.database_interface import *
from models.assignment_pool import AssignmentPool
from shared_modules.logger import trace_logging, get_logger
from shared_modules.proxy_date_time import ProxyDateTime


@trace_logging()
def load_assignment_pool_item_session_id(session_id: int):
    """DB Interface
    Loads an assignment pool item using the wherecondition provided as the filter."""

    sql = "SELECT * FROM assignment_pool WHERE sessionid = " + str(session_id)
    my_result = DatabaseInterface().select(sql)
    pool_item = AssignmentPool(my_result[0])

    return pool_item


@trace_logging()
def update_assignment_pool_item_ttl(item: AssignmentPool):
    """DB Interface
    Updates the ttl on an input assignment pool object."""

    sql = ("UPDATE assignment_pool SET ttl = '" + str(item.ttl) + "' WHERE sessionid = " + str(item.sessionid))
    my_result = DatabaseInterface().update(sql)


@trace_logging()
def update_assignment_pool_item(item: AssignmentPool):
    """DB Interface
    Updates the ttl on an input assignment pool object."""

    sql = ("UPDATE assignment_pool SET ttl = '" +
           str(item.ttl) + "', sessionid = " +
           str(item.sessionid) + ", assignedroutingnumber = '" +
           item.assignedroutingnumber + "' WHERE poolphonenumber = '" +
           item.poolphonenumber + "'")

    my_result = DatabaseInterface().update(sql)


@trace_logging()
def get_expired_pool_item_with_pool_id(poolid: int):
    """DB Interface
    This function gets the next expired pool object with matching poolid."""
    sql = "SELECT * FROM assignment_pool WHERE poolid = " + str(poolid) + " AND ttl < NOW()"

    my_result = DatabaseInterface().select(sql)
    if len(my_result) > 0:
        return AssignmentPool(my_result[0])
    else:
        return False


@trace_logging()
def refresh_ttl_for_pool_number_with_session_id(session_id: int, duration_minutes: int):
    """Composite Controller Function
    Uses a session id refresh the time window on an assignment pool number using the current
    time plus whatever the duration in minutes that is input into the function."""
    pool_item = load_assignment_pool_item_session_id(session_id)
    temp = ProxyDateTime.now() + timedelta(minutes=duration_minutes)
    pool_item.ttl = temp.strftime("%Y-%m-%d %H:%M:%S")
    update_assignment_pool_item_ttl(pool_item)

    return pool_item


@trace_logging()
def reserve_number_from_pool(session_id: int, routingnumber: str, poolid: int):
    pool_item = get_expired_pool_item_with_pool_id(poolid)
    if pool_item is False:
        return False
    else:
        pool_item.ttl = ProxyDateTime.now() + timedelta(minutes=120)
        pool_item.sessionid = session_id
        pool_item.assignedroutingnumber = routingnumber
        update_assignment_pool_item(pool_item)
        return pool_item


@trace_logging()
def set_ttl_expiry(pool_phone: str, duration_minutes: int = 10):
    sql = "SELECT * FROM assignment_pool WHERE poolphonenumber = " + str(pool_phone)
    my_result = DatabaseInterface().select(sql)

    if len(my_result) > 0:
        session_id = AssignmentPool(my_result[0]).sessionid
        return refresh_ttl_for_pool_number_with_session_id(session_id, duration_minutes)
    else:
        return False
