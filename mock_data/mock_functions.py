from shared_modules.parsed_url import ParsedUrl


def mock_assignment_pool_dict():
    data = dict()
    data['poolid'] = 1
    data['businessid'] = 2
    data['poolphonenumber'] = '123-456-7890'
    data['ttl'] = '2021-01-01 12:00:00'
    data['assignedroutingnumber'] = '098-765-4321'
    data['sessionid'] = 3
    return data


# TODO ASH This needs type checking
def mock_session_information_log_dict():
    data = dict()
    data['poolid'] = 1
    data['sessionid'] = 1
    data['businessid'] = 1
    data['numberroutedsuccessfully'] = 1
    data['replacementphonenumber'] = '123-456-7890'
    data['routingnumber'] = '123-456-7890'
    data['poolphonenumber'] = '123-456-7890'
    data['callstart'] = '2021-01-01 12:00:00'
    data['callend'] = '2021-01-01 12:00:00'
    data['clickid'] = 'NULL'
    data['clicksource'] = 'NULL'
    data['url'] = 'NULL'
    data['utm_source'] = 'NULL'
    data['utm_medium'] = 'NULL'
    data['utm_campaign'] = 'NULL'
    data['utm_adgroup'] = 'NULL'
    data['utm_keyword'] = 'NULL'
    data['utm_device'] = 'NULL'
    data['utm_brandtype'] = 'NULL'
    data['utm_content'] = 'NULL'
    data['gclsrc'] = 'NULL'
    data['gclid'] = 'NULL'
    data['fbclid'] = 'NULL'
    data['clickid'] = 'NULL'
    return data


def mock_business_config_dict():
    data = dict()
    data['businessid'] = 1
    data['active'] = True
    data['cpmaincustomer'] = True
    data['defaultttl'] = 1
    data['emailnotifications'] = True
    data['emailaddress'] = 'a@a.com"'
    data['featuretoggle'] = 1
    return data


def mock_replacement_number_map_dict():
    data = dict()
    data['replacementphonenumber'] = '111-111-2222'
    data['routingnumber'] = '111-111-2223'
    data['poolid'] = 1
    return data


# This gets mocked in the tests, but it ends up calling the ParsedUrl constructor anyway.
#  Tests run as expected regardless
def mock_parsed_url():
    parsed_url_item = ParsedUrl('www.google.com')
    parsed_url_item.url = 'www.google.com'
    parsed_url_item.utm_source = 'NULL'
    parsed_url_item.utm_medium = 'NULL'
    parsed_url_item.utm_campaign = 'NULL'
    parsed_url_item.utm_adgroup = 'NULL'
    parsed_url_item.utm_keyword = 'NULL'
    parsed_url_item.utm_device = 'NULL'
    parsed_url_item.utm_brandtype = 'NULL'
    parsed_url_item.utm_content = 'NULL'
    parsed_url_item.gclsrc = 'NULL'
    parsed_url_item.gclid = 'NULL'
    parsed_url_item.fbclid = 'NULL'
    parsed_url_item.twclid = 'NULL'
    parsed_url_item.clickid = 'NULL'
    return parsed_url_item
