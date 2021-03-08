import unittest
from unittest.mock import patch
import controllers.replacement_number_map_controller as RNMController
from mock_data.mock_functions import mock_replacement_number_map_dict


class ReplacementNumberMapControllerTest(unittest.TestCase):
    """
    unit test for replacement number map controller
    """

    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_get_replacement_map_item_with_number_to_replace(self, dbi_select):
        mock_object = mock_replacement_number_map_dict()
        mock_object['replacementphonenumber'] = '123-444-555'
        dbi_select.return_value = [mock_object]

        result = RNMController.get_replacement_map_item_with_number_to_replace('123-444-555')

        self.assertEqual(result.replacementphonenumber, '123-444-555')
        dbi_select.assert_called_with("SELECT * FROM replacementnumbermap WHERE replacementphonenumber = '123-444-555'")
