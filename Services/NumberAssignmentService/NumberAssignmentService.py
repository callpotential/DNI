import Controllers.SessionInformationLogController as session
import Controllers.AssignmentPoolController as pool
import Controllers.BusinessConfigController as business
import Controllers.ReplacementNumberMapController as map
import SharedModules.ParsedUrl as url_parser

def get_assignment_number(url:str):
    """
    main service function
    """
    parsed_url_object = url_parser.parsed_url(url)

    if not refresh_ttl_for_existing_session(parsed_url_object.clickid):
        """This will be hit if the gclid is new and not associated with a reserved number.
        Create new session info log and assign a number here or handle the situation if no numbers are available."""
    else:
        return "The number ttl was refreshed for the existing reserved number."


def refresh_ttl_for_existing_session(clickid:str):
    session_item = session.get_session_item_with_click_id(clickid)

    if session_item is not False:
        pool.refresh_ttl_for_pool_number_with_session_id(session_item.sessionid,120)
        return True
    return False

def create_session_and_reserve_number(clickid:str, number_to_replace:str, parsed_url:url_parser.parsed_url):

    #get the map object from the database for the corresponding
    map_item = map.get_replacement_map_item_with_number_to_replace(number_to_replace)
    pool_item = pool.get_expired_pool_item_with_pool_id(map_item.poolid)

    if pool_item == False:
        return False

    business_item = business.get_business_object_with_business_id(pool_item.businessid)

    session_object_dict = {'poolid': pool_item.poolid,
    'businessid': business_item.businessid,
    'numberroutedsuccessfully': 'NULL',
    'replacementphonenumber': number_to_replace,
    'routingnumber': map_item.routingnumber,
    'poolphonenumber': pool_item.poolphonenumber,
    'ttl': 'NULL',
    'callstart': "NULL",
    'callend': 'NULL',
    'clickid': 'NULL',
    'clicksource': parsed_url.utm_source,
    'url': parsed_url.url,
    'utm_source': parsed_url.utm_source,
    'utm_medium': parsed_url.utm_medium,
    'utm_campaign': parsed_url.utm_campaign,
    'utm_adgroup': parsed_url.utm_adgroup,
    'utm_keyword': parsed_url.utm_keyword,
    'utm_device': parsed_url.utm_device,
    'utm_brandtype': parsed_url.utm_brandtype,
    'utm_content': parsed_url.utm_content,
    'gclsrc': parsed_url.gclsrc,
    'gclid': parsed_url.gclid,
    'fbclid': parsed_url.fbclid,
    'clickid': parsed_url.clickid
    }

    session_item = session.create_new_session_item(session_object_dict)
    session_id = session_item.sessionid
    pool.reserve_number_from_pool(pool_item, session_id, map_item)






