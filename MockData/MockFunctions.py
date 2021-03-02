


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