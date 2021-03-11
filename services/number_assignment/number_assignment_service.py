import controllers.session_information_log_controller as session
import controllers.assignment_pool_controller as pool
import controllers.replacement_number_map_controller as map
import shared_modules.parsed_url as url_parser
from models.phone_number import PhoneNumber
from shared_modules.logger import trace_logging, get_logger
from shared_modules.proxy_date_time import ProxyDateTime


@trace_logging()
def get_assignment_pool_number(url: str, number_to_replace: PhoneNumber):
    """
    main service function
    """
    parsed_url_object = url_parser.ParsedUrl(url)

    if parsed_url_object.clickid == "NULL":
        return [map.get_replacement_map_item_with_number_to_replace(number_to_replace).routingnumber,
                "The information provided was not from a valid or supported adclick source."]

    # Check if there is a reserved pool item for this click id if there is refresh it.
    pool_item = refresh_ttl_for_existing_session(parsed_url_object.clickid)
    if pool_item is not None:
        return [pool_item.poolphonenumber, "The number ttl was refreshed for the existing reserved number."]

    # If there is no pool item found create one.
    pool_item = create_session_and_reserve_number(number_to_replace, parsed_url_object)
    if pool_item is not None:
        # If the pool item was reserved successfully return the pool item.
        return [pool_item.poolphonenumber, "A pool and session item was successfully created and reserved."]

    # If no pool item could be reserved return the routing number for the business and send an email notification.
    return [map.get_replacement_map_item_with_number_to_replace(number_to_replace).routingnumber,
            "There are no more numbers left in the pool"]


@trace_logging()
def refresh_ttl_for_existing_session(clickid: str):
    session_item = session.get_session_item_with_click_id(clickid)

    if session_item is not None:
        return pool.refresh_ttl_for_pool_number_with_session_id(session_item.sessionid, 120)
    else:
        return None


@trace_logging()
def create_session_and_reserve_number(number_to_replace: PhoneNumber, parsed_url: url_parser.ParsedUrl):
    # get the map object from the database for the corresponding
    map_item = map.get_replacement_map_item_with_number_to_replace(number_to_replace)
    pool_item = pool.get_expired_pool_item_with_pool_id(map_item.poolid)

    # There is no expired pool item, pool is full
    if pool_item is None:
        return None

    session_object_dict = {
        'sessionid': int(),
        'poolid': pool_item.poolid,
        'businessid': pool_item.businessid,
        'numberroutedsuccessfully': 'NULL',
        'replacementphonenumber': str(number_to_replace),
        'routingnumber': str(map_item.routingnumber),
        'poolphonenumber': str(pool_item.poolphonenumber),
        'callstart': ProxyDateTime.date_time_to_sql(ProxyDateTime.min),
        'callend': ProxyDateTime.date_time_to_sql(ProxyDateTime.min),
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
    return pool.reserve_number_from_pool(session_id, map_item.routingnumber, pool_item.poolid)


@trace_logging()
def handler(event, context):
    get_logger().log_handler_enter(event, context)

    url: str = event['url']
    number_to_replace: PhoneNumber = PhoneNumber(event['phone'])

    resp = get_assignment_pool_number(url, number_to_replace)

    get_logger().log_handler_exit(resp)
    return resp

get_assignment_pool_number("https://www.cubesmart.com/illinois-self-storage/chicago-self-storage/?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2Bsmart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB",
                           "234-123-4323")