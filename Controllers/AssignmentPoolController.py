import SharedModules.DatabaseConnector as db
from Models.AssignmentPool import AssignmentPool
import mysql.connector

def load_assignment_pool_item(where_clause):
    my_db = db.newConnector()
    my_cursor = my_db.cursor()

    sql = "SELECT * FROM AssignmentPool WHERE " + where_clause

    my_cursor.execute(sql)
    my_result = my_cursor.fetchall()
    pool_item = AssignmentPool(my_result[0])
    my_db.close()

load_assignment_pool_item("sessionid = 1")



def refresh_ttl_for_pool_number_with_session_id(session_id, duration_minutes):
    mydb = db.newConnector()
    mycursor = mydb.cursor()

    sql = "UPDATE AssignmentPoolController SET address = 'Canyon 123' WHERE address = 'Valley 345'"

    mycursor.execute()
    mydb.commit()
    mydb.close()
