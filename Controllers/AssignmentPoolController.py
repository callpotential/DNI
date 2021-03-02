from datetime import timedelta
from SharedModules.DatabaseInterface import *
from Models.AssignmentPool import AssignmentPool
from SharedModules.ProxyDateTime import ProxyDateTime


def load_assignment_pool_item_session_id(session_id:int):
    """DB Interface
    Loads an assignment pool item using the wherecondition provided as the filter."""

    sql = "SELECT * FROM AssignmentPool WHERE sessionid = " + str(session_id)
    my_result = DatabaseInterface().select(sql)
    pool_item = AssignmentPool(my_result[0])

    return pool_item

def update_assignment_pool_item_ttl(item:AssignmentPool):
    """DB Interface
    Updates the ttl on an input assignment pool object."""

    sql = ("UPDATE AssignmentPool SET ttl = '" + str(item.ttl) + "' WHERE sessionid = " + str(item.sessionid))
    my_result = DatabaseInterface().update(sql)

def get_expired_pool_item_with_pool_id(poolid:int):
    """DB Interface
    This function gets the next expired pool object with matching poolid."""
    sql = "SELECT * FROM AssignmentPool WHERE poolid = " + str(poolid) + " AND ttl < NOW()"

    my_result = DatabaseInterface().select(sql)
    if len(my_result) > 0:
        return AssignmentPool(my_result[0])
    else:
        return False

def refresh_ttl_for_pool_number_with_session_id(session_id:int, duration_minutes:int):
    """Composite Controller Function
    Uses a session id refresh the time window on an assignment pool number using the current
    time plus whatever the duration in minutes that is input into the function."""
    pool_item = load_assignment_pool_item_session_id(session_id)
    temp = ProxyDateTime.now() + timedelta(minutes=duration_minutes)
    pool_item.ttl = temp.strftime("%Y-%m-%d %H:%M:%S")
    update_assignment_pool_item_ttl(pool_item)


