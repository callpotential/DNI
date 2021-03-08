from datetime import datetime
import unittest
from unittest.mock import patch
from mock_data.mock_functions import mock_assignment_pool_dict
from models.assignment_pool import AssignmentPool
import controllers.assignment_pool_controller as pool


class AssignmentPoolControllerTest(unittest.TestCase):
    """
    unit test for assignment pool controller
    """

    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_load_assignment_pool_item(self, dbi_select):
        mock_object = mock_assignment_pool_dict()
        mock_object['sessionid'] = 5
        dbi_select.return_value = [mock_object]

        result = pool.load_assignment_pool_item_session_id(5)

        self.assertEqual(result.sessionid, 5)
        dbi_select.assert_called_with("SELECT * FROM assignment_pool WHERE sessionid = 5")

    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_get_expired_pool_item_when_exists(self, dbi_select):
        mock_object = mock_assignment_pool_dict()
        mock_object['poolid'] = 8
        dbi_select.return_value = [mock_object]

        result = pool.get_expired_pool_item_with_pool_id(8)

        self.assertEqual(result.poolid, 8)
        dbi_select.assert_called_with("SELECT * FROM assignment_pool WHERE poolid = 8 AND ttl < NOW()")

    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_get_expired_pool_item_when_none_exists(self, dbi_select):
        dbi_select.return_value = []

        result = pool.get_expired_pool_item_with_pool_id(9)

        self.assertFalse(result)
        dbi_select.assert_called_with("SELECT * FROM assignment_pool WHERE poolid = 9 AND ttl < NOW()")

    @patch('shared_modules.database_interface.DatabaseInterface.update')
    def test_update_assignment_pool_item_ttl(self, dbi_update):
        mock_object = mock_assignment_pool_dict()
        mock_object['ttl'] = '2020-01-01 12:00:00'
        mock_object['sessionid'] = 7

        pool.update_assignment_pool_item_ttl(AssignmentPool(mock_object))

        dbi_update.assert_called_with(
            "UPDATE assignment_pool SET ttl = '2020-01-01 12:00:00' WHERE sessionid = 7")

    @patch('shared_modules.proxy_date_time.ProxyDateTime.now')
    @patch('shared_modules.database_interface.DatabaseInterface.update')
    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_refresh_ttl_for_pool_number_with_session_id(self, dbi_select, dbi_update, date_time):
        mock_object = mock_assignment_pool_dict()
        mock_object['ttl'] = '2020-01-01 08:00:00'
        mock_object['sessionid'] = 9
        dbi_select.return_value = [mock_object]
        date_time.return_value = datetime.strptime('2020-01-01 08:00:00', '%Y-%m-%d %H:%M:%S')

        pool.refresh_ttl_for_pool_number_with_session_id(9, 120)

        dbi_select.assert_called_with('SELECT * FROM assignment_pool WHERE sessionid = 9')
        dbi_update.assert_called_with(
            "UPDATE assignment_pool SET ttl = '2020-01-01 10:00:00' WHERE sessionid = 9")

    @patch('shared_modules.database_interface.DatabaseInterface.update')
    def test_update_assignment_pool_item(self, dbi_update):
        mock_object = mock_assignment_pool_dict()
        mock_object['ttl'] = '2020-01-01 08:00:00'
        mock_object['sessionid'] = 9
        mock_object['assignedroutingnumber'] = '123-123-1234'
        mock_object['poolphonenumber'] = '123-123-1235'

        result = pool.update_assignment_pool_item(AssignmentPool(mock_object))

        dbi_update.assert_called_with("UPDATE assignment_pool SET ttl = '2020-01-01 08:00:00', sessionid = 9, assignedroutingnumber = '123-123-1234' WHERE poolphonenumber = '123-123-1235'")
        self.assertEqual(result, None)

    @patch('shared_modules.proxy_date_time.ProxyDateTime.now')
    @patch('shared_modules.database_interface.DatabaseInterface.update')
    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_reserve_number_from_pool_when_exists(self, dbi_select, dbi_update, date_time):
        mock_object = mock_assignment_pool_dict()
        mock_object['sessionid'] = 2
        mock_object['assignedroutingnumber'] = '123-456-1212'
        mock_object['poolid'] = 4
        date_time.return_value = datetime.strptime('2020-01-01 08:00:00', '%Y-%m-%d %H:%M:%S')
        dbi_select.return_value = [mock_object]

        result = pool.reserve_number_from_pool(2, '123-456-1212', 4)

        dbi_select.assert_called_with("SELECT * FROM assignment_pool WHERE poolid = 4 AND ttl < NOW()")
        dbi_update.assert_called_with("UPDATE assignment_pool SET ttl = '2020-01-01 10:00:00', sessionid = 2, assignedroutingnumber = '123-456-1212' WHERE poolphonenumber = '123-456-7890'")
        self.assertEqual(result.ttl, datetime.strptime('2020-01-01 10:00:00', '%Y-%m-%d %H:%M:%S'))
        self.assertEqual(result.sessionid, 2)
        self.assertEqual(result.assignedroutingnumber, '123-456-1212')

    @patch('shared_modules.database_interface.DatabaseInterface.select')
    def test_reserve_number_from_pool_when_none_exists(self, dbi_select):
        dbi_select.return_value = []

        result = pool.reserve_number_from_pool(3, '223-456-1212', 5)

        dbi_select.assert_called_with("SELECT * FROM assignment_pool WHERE poolid = 5 AND ttl < NOW()")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
