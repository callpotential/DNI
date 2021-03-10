import unittest
from unittest.mock import patch
import services.number_assignment.number_assignment_service as NAS
from mock_data.mock_functions import mock_session_information_log_dict, mock_parsed_url, mock_business_config_dict, \
    mock_replacement_number_map_dict, mock_assignment_pool_dict
from models.assignment_pool import AssignmentPool
from models.business_config import BusinessConfig
from models.phone_number import PhoneNumber
from models.replacement_number_map import ReplacementNumberMap
from models.session_information_log import SessionInformationLog


class NumberAssignmentServiceTest(unittest.TestCase):
    """
        This is a test for the number assignment service.
    """
    @patch('shared_modules.parsed_url.ParsedUrl')
    @patch('controllers.replacement_number_map_controller.get_replacement_map_item_with_number_to_replace')
    def test_get_assignment_pool_number_when_there_is_no_click_id(self, get_replacement, parsed_url):
        mock_url = mock_parsed_url()
        mock_url.clickid = 'NULL'
        parsed_url.return_value = mock_url
        mock_replacement_number = ReplacementNumberMap(mock_replacement_number_map_dict())
        mock_replacement_number.routingnumber = '123-112-1234'
        get_replacement.return_value = mock_replacement_number

        result = NAS.get_assignment_pool_number('www.google.com', PhoneNumber('111-111-1111'))

        self.assertEqual(result, ['123-112-1234', "The information provided was not from a valid or supported adclick source."])

    @patch('shared_modules.parsed_url.ParsedUrl')
    @patch('controllers.assignment_pool_controller.refresh_ttl_for_pool_number_with_session_id')
    @patch('controllers.session_information_log_controller.get_session_item_with_click_id')
    def test_get_assignment_pool_number_when_there_is_an_existing_session(self, get_existing_session, refresh_ttl, parsed_url):
        mock_url = mock_parsed_url()
        mock_url.clickid = 'Not NULL'
        parsed_url.return_value = mock_url
        mock_session = SessionInformationLog(mock_session_information_log_dict())
        mock_session.sessionid = 4
        get_existing_session.return_value = mock_session
        mock_pool_item = AssignmentPool(mock_assignment_pool_dict())
        mock_pool_item.poolphonenumber = '111-111-1112'
        refresh_ttl.return_value = mock_pool_item

        result = NAS.get_assignment_pool_number('www.google.com', PhoneNumber('111-111-1111'))

        self.assertEqual(result, ['111-111-1112', "The number ttl was refreshed for the existing reserved number."])
        get_existing_session.assert_called_with('Not NULL')
        refresh_ttl.assert_called_with(4, 120)

    @patch('shared_modules.parsed_url.ParsedUrl')
    @patch('controllers.replacement_number_map_controller.get_replacement_map_item_with_number_to_replace')
    @patch('controllers.assignment_pool_controller.get_expired_pool_item_with_pool_id')
    @patch('controllers.assignment_pool_controller.reserve_number_from_pool')
    @patch('controllers.session_information_log_controller.create_new_session_item')
    @patch('controllers.session_information_log_controller.get_session_item_with_click_id')
    def test_get_assignment_pool_number_when_there_is_no_existing_session(self, get_existing_session, create_new_session, reserve_number, get_expired_item, get_replacement_map, parsed_url):
        mock_url = mock_parsed_url()
        mock_url.clickid = 'Not NULL'
        parsed_url.return_value = mock_url

        get_existing_session.return_value = None

        mock_map_item = ReplacementNumberMap(mock_replacement_number_map_dict())
        mock_map_item.poolid = 2
        mock_map_item.routingnumber = PhoneNumber('121-121-1212')
        get_replacement_map.return_value = mock_map_item

        mock_pool_item = AssignmentPool(mock_assignment_pool_dict())
        mock_pool_item.poolid = 3
        get_expired_item.return_value = mock_pool_item

        mock_session = SessionInformationLog(mock_session_information_log_dict())
        mock_session.sessionid = 5
        create_new_session.return_value = mock_session

        mock_pool_item = AssignmentPool(mock_assignment_pool_dict())
        mock_pool_item.poolphonenumber = PhoneNumber('111-111-1113')
        reserve_number.return_value = mock_pool_item

        result = NAS.get_assignment_pool_number('www.google.com', PhoneNumber('111-111-1111'))

        self.assertEqual(str(result[0]), '1111111113')
        self.assertEqual(result[1], "A pool and session item was successfully created and reserved.")
        get_existing_session.assert_called_with('Not NULL')
        create_new_session.assert_called()  # The dict that it's called with is hard coded and would look nasty in here
        reserve_number.assert_called_with(5, mock_map_item.routingnumber, 3)

    @patch('shared_modules.parsed_url.ParsedUrl')
    @patch('controllers.replacement_number_map_controller.get_replacement_map_item_with_number_to_replace')
    @patch('controllers.assignment_pool_controller.get_expired_pool_item_with_pool_id')
    @patch('controllers.assignment_pool_controller.reserve_number_from_pool')
    @patch('controllers.session_information_log_controller.create_new_session_item')
    @patch('controllers.session_information_log_controller.get_session_item_with_click_id')
    def test_get_assignment_pool_number_when_there_is_no_existing_session_and_pool_empty(self, get_existing_session, create_new_session, reserve_number, get_expired_item, get_replacement_map, parsed_url):
        mock_url = mock_parsed_url()
        mock_url.clickid = 'Not NULL'
        parsed_url.return_value = mock_url

        get_existing_session.return_value = None

        mock_map_item = ReplacementNumberMap(mock_replacement_number_map_dict())
        mock_map_item.poolid = 2
        mock_map_item.routingnumber = '121-121-1212'
        get_replacement_map.return_value = mock_map_item

        mock_pool_item = AssignmentPool(mock_assignment_pool_dict())
        mock_pool_item.poolid = 3
        get_expired_item.return_value = mock_pool_item

        mock_session = SessionInformationLog(mock_session_information_log_dict())
        mock_session.sessionid = 5
        create_new_session.return_value = mock_session

        reserve_number.return_value = None


        result = NAS.get_assignment_pool_number('www.google.com', PhoneNumber('111-111-1111'))

        self.assertEqual(result, ['121-121-1212', "There are no more numbers left in the pool"])
        get_existing_session.assert_called_with('Not NULL')
        create_new_session.assert_called()  # The dict that it's called with is hard coded and would look nasty in here
        reserve_number.assert_called_with(5, '121-121-1212', 3)

    @patch('controllers.assignment_pool_controller.refresh_ttl_for_pool_number_with_session_id')
    @patch('controllers.session_information_log_controller.get_session_item_with_click_id')
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

    @patch('controllers.assignment_pool_controller.refresh_ttl_for_pool_number_with_session_id')
    @patch('controllers.session_information_log_controller.get_session_item_with_click_id')
    def test_should_return_false_when_no_existing_session(self, get_session_item, refresh_ttl):
        click_id = '?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2B' \
            'smart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0' \
            'nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB'
        get_session_item.return_value = None

        result = NAS.refresh_ttl_for_existing_session(click_id)

        self.assertFalse(result)
        get_session_item.assert_called_with(click_id)
        refresh_ttl.assert_not_called

    @patch('controllers.replacement_number_map_controller.get_replacement_map_item_with_number_to_replace')
    @patch('controllers.assignment_pool_controller.get_expired_pool_item_with_pool_id')
    def test_should_return_false_when_no_existing_session(self, get_expired_item, get_replacement_map):
        parsed_url = mock_parsed_url()
        get_replacement_map.return_value = ReplacementNumberMap(mock_replacement_number_map_dict())
        get_expired_item.return_value = None

        result = NAS.create_session_and_reserve_number(PhoneNumber('111-222-3434'), parsed_url)

        self.assertFalse(result)

    @patch('controllers.replacement_number_map_controller.get_replacement_map_item_with_number_to_replace')
    @patch('controllers.assignment_pool_controller.get_expired_pool_item_with_pool_id')
    @patch('controllers.assignment_pool_controller.reserve_number_from_pool')
    @patch('controllers.business_config_controller.get_business_object_with_business_id')
    @patch('controllers.session_information_log_controller.create_new_session_item')
    def test_should_return_false_when_pool_is_full(self, create_session_item, get_business_object, reserve_number, get_expired_item, get_replacement_map):
        parsed_url = mock_parsed_url()
        get_replacement_map.return_value = ReplacementNumberMap(mock_replacement_number_map_dict())
        get_expired_item.return_value = AssignmentPool(mock_assignment_pool_dict())
        get_business_object.return_value = BusinessConfig(mock_business_config_dict())
        create_session_item.return_value = SessionInformationLog(mock_session_information_log_dict())
        reserve_number.return_value = None

        result = NAS.create_session_and_reserve_number(PhoneNumber('111-222-3434'), parsed_url)

        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
