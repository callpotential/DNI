import unittest
from unittest.mock import patch
import controllers.session_information_log_controller as session
from mock_data.mock_functions import mock_session_information_log_dict
from models.session_information_log import SessionInformationLog


class SessionInformationLogControllerTest(unittest.TestCase):

    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_valid_click_id(self, dbi_select):
        click_id = \
            '?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2B' \
            'smart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0' \
            'nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB'
        item = mock_session_information_log_dict()
        item['clickid'] = click_id
        dbi_select.return_value = [item]

        result = session.get_session_item_with_click_id(click_id)

        self.assertEqual(result.clickid, click_id)

    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_invalid_click_id(self, dbi_select):
        dbi_select.return_value = []

        result = session.get_session_item_with_click_id('not valid click id')
        self.assertFalse(result)

    @patch('shared_modules.database_interface.DatabaseInterface.insert')
    def test_create_new_session_item(self, dbi_insert):
        dbi_insert.return_value = 1234

        result = session.create_new_session_item(mock_session_information_log_dict())

        self.assertEqual(result.sessionid, 1234)
        dbi_insert.assert_called_with("INSERT INTO session_information_log ( `poolid`, `businessid`, `numberroutedsuccessfully`, `replacementphonenumber`, `routingnumber`, `poolphonenumber`, `callstart`, `callend`, `clicksource`, `url`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_adgroup`, `utm_keyword`, `utm_device`, `utm_brandtype`, `utm_content`, `gclsrc`, `gclid`, `fbclid`, `clickid` ) VALUES ( 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'test' );")

    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_get_routing_num_from_pool_num(self, dbi_select):
        mock_session_info_item = mock_session_information_log_dict()
        mock_session_info_item['routingnumber'] = '765-867-5309'
        dbi_select.return_value = [mock_session_info_item]

        result = session.get_routing_number_from_pool_number('12')

        self.assertEqual(result, '765-867-5309')
        dbi_select.assert_called_with("SELECT * FROM session_information_log WHERE poolphonenumber = '12'")

    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_get_routing_num_when_no_pool_num(self, dbi_select):
        dbi_select.return_value = []

        result = session.get_routing_number_from_pool_number('13')

        self.assertEqual(result, False)
        dbi_select.assert_called_with("SELECT * FROM session_information_log WHERE poolphonenumber = '13'")


if __name__ == '__main__':
    unittest.main()
