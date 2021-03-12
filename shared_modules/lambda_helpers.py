import json


class MissingParameterException(Exception):
    pass


class InvalidParameterException(Exception):
    pass


def validate_parameter(event, parameter_name: str, parameter_type: type):
    if event[parameter_name] is None:
        raise MissingParameterException('')

    if type(event[parameter_name]) is not parameter_type:
        raise InvalidParameterException()

    return event[parameter_name]


def rest_response(code: int, message=''):
    return {
        'statusCode': code,
        'body': json.dumps(message)
    }


def rest_success_response(message='Success!'):
    return rest_response(200, message)


def json_to_xml(response: str):
    return {
        "body": response
    }
