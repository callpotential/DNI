import unittest
from shared_modules.parsed_url import ParsedUrl


class ParsedUrlTest(unittest.TestCase):
    """
        This is a test for the number assignment service.
    """
    def test_parse_no_clid(self):
        result = ParsedUrl("www.google.com")

        self.assertEqual(result.gclid, 'NULL')
        self.assertEqual(result.fbclid, 'NULL')
        self.assertEqual(result.twclid, 'NULL')
        self.assertEqual(result.clickid, 'NULL')

    def test_parse_gclid(self):
        result = ParsedUrl("www.google.com?gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB")

        self.assertEqual(result.gclid, 'Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB')
        self.assertEqual(result.fbclid, 'NULL')
        self.assertEqual(result.twclid, 'NULL')
        self.assertEqual(result.clickid, 'Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB')

    def test_parse_fbclid(self):
        result = ParsedUrl("www.google.com?fbclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB")

        self.assertEqual(result.gclid, 'NULL')
        self.assertEqual(result.fbclid, 'Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB')
        self.assertEqual(result.twclid, 'NULL')
        self.assertEqual(result.clickid, 'Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB')

    def test_parse_twclid(self):
        result = ParsedUrl("www.google.com?twclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB")

        self.assertEqual(result.gclid, 'NULL')
        self.assertEqual(result.fbclid, 'NULL')
        self.assertEqual(result.twclid, 'Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB')
        self.assertEqual(result.clickid, 'Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB')

