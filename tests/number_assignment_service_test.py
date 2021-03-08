import unittest
from unittest.mock import patch
import services.number_assignment.number_assignment_service as NAS
from mock_data.mock_functions import mock_session_information_log_dict, mock_parsed_url, mock_business_config_dict, \
    mock_replacement_number_map_dict, mock_assignment_pool_dict
from models.assignment_pool import AssignmentPool
from models.business_config import BusinessConfig
from models.replacement_number_map import ReplacementNumberMap
from models.session_information_log import SessionInformationLog


class NumberAssignmentServiceTest(unittest.TestCase):
    """
        This is a test for the number assignment service.
    """
    @patch('controllers.AssignmentPoolController.refresh_ttl_for_pool_number_with_session_id')
    @patch('controllers.SessionInformationLogController.get_session_item_with_click_id')
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

    @patch('controllers.AssignmentPoolController.refresh_ttl_for_pool_number_with_session_id')
    @patch('controllers.SessionInformationLogController.get_session_item_with_click_id')
    def test_should_return_false_when_no_existing_session(self, get_session_item, refresh_ttl):
        click_id = '?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2B' \
            'smart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0' \
            'nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB'
        get_session_item.return_value = False

        result = NAS.refresh_ttl_for_existing_session(click_id)

        self.assertFalse(result)
        get_session_item.assert_called_with(click_id)
        refresh_ttl.assert_not_called

    @patch('controllers.ReplacementNumberMapController.get_replacement_map_item_with_number_to_replace')
    @patch('controllers.AssignmentPoolController.get_expired_pool_item_with_pool_id')
    def test_should_return_false_when_no_existing_session(self, get_expired_item, get_replacement_map):
        parsed_url = mock_parsed_url()
        get_replacement_map.return_value = ReplacementNumberMap(mock_replacement_number_map_dict())
        get_expired_item.return_value = False

        result = NAS.create_session_and_reserve_number('111-222-3434', parsed_url)

        self.assertFalse(result)

    @patch('controllers.ReplacementNumberMapController.get_replacement_map_item_with_number_to_replace')
    @patch('controllers.AssignmentPoolController.get_expired_pool_item_with_pool_id')
    @patch('controllers.AssignmentPoolController.reserve_number_from_pool')
    @patch('controllers.BusinessConfigController.get_business_object_with_business_id')
    @patch('controllers.SessionInformationLogController.create_new_session_item')
    def test_should_return_false_when_pool_is_full(self, create_session_item, get_business_object,
                                                          reserve_number, get_expired_item, get_replacement_map):
        parsed_url = mock_parsed_url()
        get_replacement_map.return_value = ReplacementNumberMap(mock_replacement_number_map_dict())
        get_expired_item.return_value = AssignmentPool(mock_assignment_pool_dict())
        get_business_object.return_value = BusinessConfig(mock_business_config_dict())
        create_session_item.return_value = SessionInformationLog(mock_session_information_log_dict())
        reserve_number.return_value = False

        result = NAS.create_session_and_reserve_number('111-222-3434', parsed_url)

        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
