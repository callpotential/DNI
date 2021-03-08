import unittest
from unittest.mock import patch
import controllers.session_information_log_controller as session
from mock_data.mock_functions import mock_session_information_log_dict


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


if __name__ == '__main__':
    unittest.main()
