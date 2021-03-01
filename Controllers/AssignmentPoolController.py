from datetime import datetime
from datetime import timedelta
import SharedModules.DatabaseConnector as db
from Models.AssignmentPool import AssignmentPool

def load_assignment_pool_item(where_condition):
    """DB Interface
    Loads an assignment pool item using the wherecondition provided as the filter."""
    my_db = db.newConnector()
    my_cursor = my_db.cursor(dictionary=True, buffered=True)

    sql = "SELECT * FROM AssignmentPool WHERE " + where_condition

    my_cursor.execute(sql)
    my_result = my_cursor.fetchall()
    pool_item = AssignmentPool(my_result[0])
    my_db.close()

    return pool_item


def update_assignment_pool_item_ttl(item:AssignmentPool):
    """DB Interface
    Updates the ttl on an input assignment pool object."""
    mydb = db.newConnector()
    mycursor = mydb.cursor()

    sql = ("UPDATE AssignmentPool SET ttl = '" + str(item.ttl) + "' WHERE sessionid = " + str(item.sessionid))

    mycursor.execute(sql)
    mydb.commit()
    mydb.close()

def refresh_ttl_for_pool_number_with_session_id(session_id, duration_minutes):
    """Composite Controller Function
    Uses a session id refresh the time window on an assignment pool number using the current
    time plus whatever the duration in minutes that is input into the function."""
    pool_item = load_assignment_pool_item("sessionid = " + str(session_id))
    temp = datetime.now() + timedelta(minutes=duration_minutes)
    pool_item.ttl = temp.strftime("%Y-%m-%d %H:%M:%S")
    update_assignment_pool_item_ttl(pool_item)
