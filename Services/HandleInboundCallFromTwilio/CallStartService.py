import Controllers.AssignmentPoolController as pool
import Controllers.SessionInformationLogController as session

def update_session_with_call_start(phone_number):
    if pool.is_phone_number_active(phone_number):
        session.set_call_start_for_session(phone_number)
        return "Session call start time updated."
    elif:
        return "Phone number is not active."
