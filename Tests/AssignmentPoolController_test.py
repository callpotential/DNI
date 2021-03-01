from datetime import datetime
from datetime import timedelta
import unittest
import SharedModules.DatabaseInterface as db
from Models.AssignmentPool import AssignmentPool
import Controllers.AssignmentPoolController as pool


class AssignmentPoolControllerTest(unittest.TestCase):
    """
    unit test for assignment pool controller
    """
    def test_load_assignment_pool_item(self):
        assert pool.load_assignment_pool_item("sessionid = 1")

    def test_update_assignment_pool_item_ttl(self):
        pool.refresh_ttl_for_pool_number_with_session_id(1, 0)



        my_db = db.newConnector()
        my_cursor = my_db.cursor()
        sql = "SELECT ttl FROM AssignmentPool WHERE sessionid = 1"
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()
        before_time = my_result[0]
        my_db.close()

        pool_item = pool.load_assignment_pool_item("sessionid = 1")
        temp = datetime.now() + timedelta(minutes=120)
        pool_item.ttl = temp.strftime("%Y-%m-%d %H:%M:%S")
        print(pool_item.ttl)
        pool.update_assignment_pool_item_ttl(pool_item)

        my_db = db.newConnector()
        my_cursor = my_db.cursor()
        sql = "SELECT ttl FROM AssignmentPool WHERE sessionid = 1"
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()
        after_time = my_result[0]
        my_db.close()

        print(after_time)
        print(before_time)

        assert after_time != before_time

    def test_refresh_ttl_for_pool_number_with_session_id(self):
        my_db = db.newConnector()
        my_cursor = my_db.cursor()
        sql = "SELECT ttl FROM AssignmentPool WHERE sessionid = 1"
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()
        before_time = my_result[0]
        my_db.close()

        pool.refresh_ttl_for_pool_number_with_session_id(1,120)

        my_db = db.newConnector()
        my_cursor = my_db.cursor()
        sql = "SELECT ttl FROM AssignmentPool WHERE sessionid = 1"
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()
        after_time = my_result[0]
        my_db.close()

        assert after_time != before_time

if __name__ == '__main__':
    unittest.main()
