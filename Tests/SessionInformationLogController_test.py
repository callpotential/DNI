import unittest
import Controllers.SessionInformationLogController as session

class MyTestCase(unittest.TestCase):
    def test_valid_click_id(self):
        assert session.get_session_item_with_click_id(
            '?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2B'
            'smart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0'
            'nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB'
        )
    def test_invalid_click_id(self):
        response = session.get_session_item_with_click_id('not valid click id')
        assert response == False


if __name__ == '__main__':
    unittest.main()
