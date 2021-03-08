import controllers.session_information_log_controller as session
import controllers.assignment_pool_controller as pool
import controllers.business_config_controller as business
import controllers.replacement_number_map_controller as map
import shared_modules.parsed_url as url_parser
from shared_modules.logger import trace_logging
from shared_modules.proxy_date_time import ProxyDateTime

@trace_logging()
def get_assignment_pool_number(url:str, number_to_replace:str):
    """
    main service function
    """
    parsed_url_object = url_parser.ParsedUrl(url)

    if parsed_url_object.clickid == "NULL":
        return [map.get_replacement_map_item_with_number_to_replace(number_to_replace).routingnumber,
               "The information provided was not from a valid or supported adclick source."]

    #Check if there is a reserved pool item for this click id if there is refresh it.
    pool_item = refresh_ttl_for_existing_session(parsed_url_object.clickid)
    if not pool_item:
        #If there is no pool item found create one.
        pool_item = create_session_and_reserve_number(number_to_replace, parsed_url_object)
        if pool_item != False:
            #If the pool item was reserved successfully return the pool item.
            return [pool_item.poolphonenumber, "A pool and session item was successfully created and reserved."]
        else:
            #If no pool item could be reserved return the routing number for the business and send an email notification.
            return [map.get_replacement_map_item_with_number_to_replace(number_to_replace).routingnumber, "There are no more numbers left in the pool"]
    else:
        return [pool_item.poolphonenumber, "The number ttl was refreshed for the existing reserved number."]


@trace_logging()
def refresh_ttl_for_existing_session(clickid:str):
    session_item = session.get_session_item_with_click_id(clickid)

    if session_item is not False:
        return pool.refresh_ttl_for_pool_number_with_session_id(session_item.sessionid,120)
    return False

@trace_logging()
def create_session_and_reserve_number(number_to_replace:str, parsed_url:url_parser.ParsedUrl):

    #get the map object from the database for the corresponding
    map_item = map.get_replacement_map_item_with_number_to_replace(number_to_replace)
    pool_item = pool.get_expired_pool_item_with_pool_id(map_item.poolid)

    if pool_item == False:
        return False

    business_item = business.get_business_object_with_business_id(pool_item.businessid)

    session_object_dict = {
    'sessionid': int(),
    'poolid': pool_item.poolid,
    'businessid': business_item.businessid,
    'numberroutedsuccessfully': 'NULL',
    'replacementphonenumber': number_to_replace,
    'routingnumber': map_item.routingnumber,
    'poolphonenumber': pool_item.poolphonenumber,
    'callstart': ProxyDateTime.min.strftime("%Y-%m-%d %H:%M:%S"),
    'callend': ProxyDateTime.min.strftime("%Y-%m-%d %H:%M:%S"),
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
    reserved_pool_item = pool.reserve_number_from_pool(session_id, map_item.routingnumber, pool_item.poolid)

    if reserved_pool_item == False:
        #pool is full
        return False
    else:
        return reserved_pool_item


