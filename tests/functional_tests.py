from controllers.assignment_pool_controller import load_assignment_pool_item_session_id
from models.phone_number import PhoneNumber
from services.number_assignment.number_assignment_service import get_assignment_pool_number
#from services.request_pool_numbers.lambda_function import lambda_handler
#
# get_assignment_pool_number("https://www.cubesmart.com/illinois-self-storage/chicago-self-storage/?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2Bsmart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB",
#                            PhoneNumber("234-123-4323"))
from services.request_pool_numbers.lambda_function import lambda_handler as request_numbers

# event = dict()
# event['pool_size'] = '5'
# event['area_code'] = '773'
# event['locality'] = ''
#
# print(request_numbers(event, None))


from services.reserve_number_pool.lambda_function import lambda_handler as reserve_number_pool
from services.number_assignment.lambda_function import lambda_handler as number_assignment
from services.handle_inbound_call_end_from_twilio.lambda_function import lambda_handler as end_call
from services.handle_inbound_call_from_twilio.lambda_function import lambda_handler as answer_call

# event = dict()
# event['replace_num'] = '765-452-4951'
# event['routing_num'] = '765-434-3461'
# event['requested_numbers'] = "[\"+17739854608\"]"
# event['business_id'] = '1290394444'
# print(reserve_number_pool(event, None))


# event = dict()
# event['url'] = 'www.google.com?gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB'
# event['phone'] = '765-452-4951'
# print(number_assignment(event, None))

# event = dict()
# event['to'] = '2342234001'
# print(end_call(event, None))


# event = dict()
# event['to'] = '2342234001'
# print(answer_call(event, None))


# event = dict()
# event['body'] = 'Called=%2B17658964609&ToState=IN&CallerCountry=US&Direction=inbound&Timestamp=Fri%2C%2012%20Mar%202021%2016%3A29%3A59%20%2B0000&CallbackSource=call-progress-events&CallerState=IN&ToZip=47303&SequenceNumber=0&To=%2B17658964609&CallSid=CAefeb0c6d4468a39213da60f1b25159cd&ToCountry=US&CallerZip=47907&CalledZip=47303&ApiVersion=2010-04-01&CallStatus=completed&CalledCity=MUNCIE&Duration=1&From=%2B17655867274&CallDuration=10&AccountSid=AC99cc9b8bf49b325289f896b2bb86c7d6&CalledCountry=US&CallerCity=LAFAYETTE&ToCity=MUNCIE&FromCountry=US&Caller=%2B17655867274&FromCity=LAFAYETTE&CalledState=IN&FromZip=47907&FromState=IN'
# print(end_call(event, None))
