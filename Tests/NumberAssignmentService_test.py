"""

"""

import unittest
from unittest.mock import patch

import Services.NumberAssignmentService.NumberAssignmentService as NAS
import SharedModules.DatabaseInterface as db
from Models.SessionInformationLog import SessionInformationLog


def MockSessionInformationLog():
    data = dict()
    data['sessionid'] = 1
    data['poolid'] = 2
    data['businessid'] = 3
    data['numberroutedsuccessfully'] = True
    data['replacementphonenumber'] = '123-444-5555'
    data['routingnumber'] = '123-444-5556'
    data['poolphonenumber'] = '123-444-5557'
    data['ttl'] = '2021-01-01 11:00:00'
    data['callstart'] = '2021-01-01 8:00:00'
    data['callend'] = '2021-01-01 9:00:00'
    data['clickid'] = 1
    data['clicksource'] = 1
    data['url'] = 'www.google.com'
    return SessionInformationLog(data)


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

    @patch('Controllers.AssignmentPoolController.refresh_ttl_for_pool_number_with_session_id')
    @patch('Controllers.SessionInformationLogController.get_session_item_with_click_id')
    def test_should_return_false_when_no_existing_session(self, get_session_item, refresh_ttl):
        session_item.sessionid = None
        get_session_item.return_value = session_item

        result = NAS.refresh_ttl_for_existing_session(
            '?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2B'
            'smart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0'
            'nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB')

        self.assertFalse(result)
        refresh_ttl.assert_not_called


if __name__ == '__main__':
    unittest.main()
