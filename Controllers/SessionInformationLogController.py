import SharedModules.DatabaseConnector as db
import Models.SessionInformationLog as session

def get_session_item_with_click_id(clickid:str):
    """DB Interface
    This function will reach out to the database and get a session item using the click id.
    """
    my_db = db.newConnector()
    my_cursor = my_db.cursor(dictionary=True, buffered=True)

    sql = "SELECT * FROM SessionInformationLog WHERE clickid = '" + clickid + "'"

    my_cursor.execute(sql)
    my_result = my_cursor.fetchall()
    my_db.close()

    if my_result:
        session_item = session.SessionInformationLog(my_result[0])
        return session_item
    else:
        return False