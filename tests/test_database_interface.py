import unittest
from unittest.mock import patch
from shared_modules.database_interface import DatabaseInterface


# Code coverage on this is lacking because it's just a facade
class DatabaseInterfaceTest(unittest.TestCase):
    """
        This is a test for the number assignment service.
    """
    @patch('shared_modules.database_interface.new_connector')
    def test_get_database(self, new_connector):
        interface = DatabaseInterface()
        result = interface.get_database()

        new_connector.assert_called()
        self.assertNotEqual(result, None)

    @patch('shared_modules.database_interface.new_connector')
    def test_get_database_is_same_across_calls(self, new_connector):
        interface = DatabaseInterface()
        result1 = interface.get_database()
        result2 = interface.get_database()

        new_connector.assert_called()
        self.assertEqual(result1, result2)

    @patch('shared_modules.database_interface.new_connector')
    def test_close_database(self, new_connector):
        interface = DatabaseInterface()
        interface.get_database()
        interface.close_database()
        interface.close_database()  # sneak in an extra line of code coverage

        new_connector.assert_called()
        self.assertEqual(interface.db, None)

    @patch('shared_modules.database_interface.new_connector')
    def test_select_database(self, new_connector):
        interface = DatabaseInterface()
        interface.select("test")

        new_connector.assert_called()
        self.assertEqual(interface.db, None)

    @patch('shared_modules.database_interface.new_connector')
    def test_update_database(self, new_connector):
        interface = DatabaseInterface()
        interface.update("test")

        new_connector.assert_called()
        self.assertEqual(interface.db, None)

    @patch('shared_modules.database_interface.new_connector')
    def test_insert_database(self, new_connector):
        interface = DatabaseInterface()
        interface.insert("test")

        new_connector.assert_called()
        self.assertEqual(interface.db, None)
