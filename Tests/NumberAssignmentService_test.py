"""

"""
import unittest
from unittest.mock import patch
import Services.NumberAssignmentService.NumberAssignmentService as NAS
from MockData.MockFunctions import mock_session_information_log_dict
from Models.SessionInformationLog import SessionInformationLog


class MyTestCase(unittest.TestCase):
    """

    """
    @patch('Controllers.AssignmentPoolController.refresh_ttl_for_pool_number_with_session_id')
    @patch('Controllers.SessionInformationLogController.get_session_item_with_click_id')
    def test_should_return_true_when_existing_session(self, get_session_item, refresh_ttl):
        click_id = '?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2B' \
            'smart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0' \
            'nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB'
        session_item = SessionInformationLog(mock_session_information_log_dict())
        session_item.sessionid = 10
        get_session_item.return_value = session_item

        result = NAS.refresh_ttl_for_existing_session(click_id)

        self.assertTrue(result)
        get_session_item.assert_called_with(click_id)
        refresh_ttl.assert_called_with(10, 120)

    @patch('Controllers.AssignmentPoolController.refresh_ttl_for_pool_number_with_session_id')
    @patch('Controllers.SessionInformationLogController.get_session_item_with_click_id')
    def test_should_return_false_when_no_existing_session(self, get_session_item, refresh_ttl):
        click_id = '?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2B' \
            'smart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0' \
            'nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB'
        get_session_item.return_value = False

        result = NAS.refresh_ttl_for_existing_session(click_id)

        self.assertFalse(result)
        get_session_item.assert_called_with(click_id)
        refresh_ttl.assert_not_called


if __name__ == '__main__':
    unittest.main()
