from datetime import datetime
import unittest
from unittest.mock import patch
from Models.AssignmentPool import AssignmentPool
import Controllers.AssignmentPoolController as pool


def mock_assignment_pool_dict():
    data = dict()
    data['poolid'] = 1
    data['businessid'] = 2
    data['poolphonenumber'] = '123-456-7890'
    data['ttl'] = '2021-01-01 12:00:00'
    data['assignedroutingnumber'] = '098-765-4321'
    data['sessionid'] = 3
    return data


class AssignmentPoolControllerTest(unittest.TestCase):
    """
    unit test for assignment pool controller
    """

    @patch('SharedModules.DatabaseInterface.DatabaseInterface.select')
    def test_load_assignment_pool_item(self, dbi_select):
        mock_object = mock_assignment_pool_dict()
        mock_object['sessionid'] = 5
        dbi_select.return_value = [mock_object]

        result = pool.load_assignment_pool_item("sessionid = 5")

        self.assertEqual(result.sessionid, 5)
        dbi_select.assert_called_with("SELECT * FROM AssignmentPool WHERE sessionid = 5")

    @patch('SharedModules.DatabaseInterface.DatabaseInterface.update')
    def test_update_assignment_pool_item_ttl(self, dbi_update):
        mock_object = mock_assignment_pool_dict()
        mock_object['ttl'] = '2020-01-01 12:00:00'
        mock_object['sessionid'] = 7

        pool.update_assignment_pool_item_ttl(AssignmentPool(mock_object))

        dbi_update.assert_called_with(
            "UPDATE AssignmentPool SET ttl = '2020-01-01 12:00:00' WHERE sessionid = 7")

    @patch('SharedModules.ProxyDateTime.ProxyDateTime.now')
    @patch('SharedModules.DatabaseInterface.DatabaseInterface.update')
    @patch('SharedModules.DatabaseInterface.DatabaseInterface.select')
    def test_refresh_ttl_for_pool_number_with_session_id(self, dbi_select, dbi_update, date_time):
        mock_object = mock_assignment_pool_dict()
        mock_object['ttl'] = '2020-01-01 08:00:00'
        mock_object['sessionid'] = 9
        dbi_select.return_value = [mock_object]
        date_time.return_value = datetime.strptime('2020-01-01 08:00:00', '%Y-%m-%d %H:%M:%S')

        pool.refresh_ttl_for_pool_number_with_session_id(9, 120)

        dbi_select.assert_called_with('SELECT * FROM AssignmentPool WHERE sessionid = 9')
        dbi_update.assert_called_with(
            "UPDATE AssignmentPool SET ttl = '2020-01-01 10:00:00' WHERE sessionid = 9")


if __name__ == '__main__':
    unittest.main()
