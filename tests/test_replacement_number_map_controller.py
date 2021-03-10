import unittest
from unittest.mock import patch
import controllers.replacement_number_map_controller as RNMController
from mock_data.mock_functions import mock_replacement_number_map_dict
from models.replacement_number_map import ReplacementNumberMap


class ReplacementNumberMapControllerTest(unittest.TestCase):
    """
    unit test for replacement number map controller
    """

    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_get_replacement_map_item_with_number_to_replace(self, dbi_select):
        mock_object = mock_replacement_number_map_dict()
        mock_object['replacementphonenumber'] = '123-444-5555'
        dbi_select.return_value = [mock_object]

        result = RNMController.get_replacement_map_item_with_number_to_replace('123-444-5555')

        self.assertEqual(result.replacementphonenumber.get_with_dashes(), '123-444-5555')
        dbi_select.assert_called_with("SELECT * FROM replacementnumbermap WHERE replacementphonenumber = '123-444-5555'")

    @patch('shared_modules.database_interface.DatabaseInterface.insert')
    def test_insert_replacement_map(self, dbi_insert):
        dbi_insert.return_value = 11123

        item = ReplacementNumberMap(mock_replacement_number_map_dict())
        item.replacementphonenumber = '123-123-4321'
        item.routingnumber = '123-123-4332'
        item.poolid = '123'
        result = RNMController.insert_replacement_map(item)

        self.assertEqual(result, 11123)
        dbi_insert.assert_called_with("INSERT INTO replacementnumbermap ( replacementphonenumber, routingnumber, poolid ) VALUES ( '123-123-4321', '123-123-4332', '123' );")
