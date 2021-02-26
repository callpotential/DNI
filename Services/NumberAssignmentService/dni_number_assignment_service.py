"""

"""
import Controllers.SessionInformationLogController as session
import Controllers.AssignmentPoolController as pool

def get_assignment_number(gclid:str):
    """

    """

    if not refresh_ttl_for_existing_session(gclid):
        """This will be hit if the gclid is new and not associated with a reserved number.
        Create new session info log and assign a number here or handle the situation if no numbers are available."""
    else:
        return "The number ttl was refreshed for the existing reserved number."


def refresh_ttl_for_existing_session(gclid:str):
    session_id = session.get_session_id_with_click_id(gclid)

    if session_id not None:
        pool.refresh_ttl_for_pool_number_with_session_id(session_id,120)
        return True
    return False