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
    session_id = session.get_session_item_with_click_id(clickid).sessionid

    if session_id is not None:
        pool.refresh_ttl_for_pool_number_with_session_id(session_id,120)
        return True
    return False

def create_session_and_reserve_number(clickid:str, number_to_replace:str, parsed_url:url_parser.parsed_url):
    map_item = map.get_replacement_map_item_with_number_to_replace(number_to_replace)
    business_item = business.get_business_object_with_business_id(map_item.businessid)
    session_item = session.create_new_session_item(clickid,business_item.businessid,map_item,parsed_url)
    session_id = session_item.sessionid
    pool.reserve_number_from_pool(session_id, map_item)






