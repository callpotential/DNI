import json


def rest_response(code: int, message: str = ''):
    return {
        'statusCode': code,
        'body': json.dumps(message)
    }


def rest_success_response(message: str = 'Success!'):
    return rest_response(200, message)


def json_to_xml(response: str):
    return {
        "body": response
    }
