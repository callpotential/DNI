"""

"""

import unittest
import Services.NumberAssignmentService.NumberAssignmentService as NAS
import SharedModules.DatabaseConnector as db

class MyTestCase(unittest.TestCase):
    """

    """
    def test_refresh_ttl_for_existing_session(self):

        my_db = db.newConnector()
        my_cursor = my_db.cursor()
        sql = "SELECT ttl FROM AssignmentPool WHERE sessionid = 1"
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()
        before_time = my_result[0]
        my_db.close()

        NAS.refresh_ttl_for_existing_session(
            '?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2B'
            'smart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0'
            'nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB')

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
