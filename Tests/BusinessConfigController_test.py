import unittest
from unittest.mock import patch
import Controllers.BusinessConfigController as BConfig
from MockData.MockFunctions import mock_business_config_dict


class BusinessConfigControllerTest(unittest.TestCase):
    """
    unit test for business config controller
    """

    @patch('SharedModules.DatabaseInterface.DatabaseInterface.select')
    def test_get_business_object_with_business_id(self, dbi_select):
        mock_object = mock_business_config_dict()
        mock_object['businessid'] = 4
        dbi_select.return_value = [mock_object]

        result = BConfig.get_business_object_with_business_id(4)

        self.assertEqual(result.businessid, 4)
        dbi_select.assert_called_with("SELECT * FROM BusinessConfig WHERE businessid = 4")