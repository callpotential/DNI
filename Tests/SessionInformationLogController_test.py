import unittest
from unittest.mock import patch
import Controllers.SessionInformationLogController as session
from Models.SessionInformationLog import SessionInformationLog


# TODO ASH This needs type checking
def mock_session_information_log_dict():
    data = dict()
    data['poolid'] = 1
    data['sessionid'] = 1
    data['businessid'] = 1
    data['numberroutedsuccessfully'] = 1
    data['replacementphonenumber'] = 1
    data['routingnumber'] = 1
    data['poolphonenumber'] = 1
    data['callstart'] = 1
    data['callend'] = 1
    data['clickid'] = 1
    data['clicksource'] = 1
    data['url'] = 1
    data['utm_source'] = 1
    data['utm_medium'] = 1
    data['utm_campaign'] = 1
    data['utm_adgroup'] = 1
    data['utm_keyword'] = 1
    data['utm_device'] = 1
    data['utm_brandtype'] = 1
    data['utm_content'] = 1
    data['gclsrc'] = 1
    data['gclid'] = 1
    data['fbclid'] = 1
    data['clickid'] = 'test'
    return data


class MyTestCase(unittest.TestCase):

    @patch('SharedModules.DatabaseInterface.DatabaseInterface.select')
    def test_valid_click_id(self, dbi_select):
        click_id = \
            '?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2B' \
            'smart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0' \
            'nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB'
        item = mock_session_information_log_dict()
        item['clickid'] = click_id
        dbi_select.return_value = [item]

        result = session.get_session_item_with_click_id(click_id)

        self.assertEquals(result.clickid, click_id)

    @patch('SharedModules.DatabaseInterface.DatabaseInterface.select')
    def test_invalid_click_id(self, dbi_select):
        dbi_select.return_value = []

        result = session.get_session_item_with_click_id('not valid click id')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
