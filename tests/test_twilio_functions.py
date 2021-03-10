import unittest
from unittest.mock import patch

from twilio.rest.api.v2010.account import IncomingPhoneNumberList

from shared_modules.twilio_functions import PhoneNumberService


# TODO ASH Figure out how to properly mock these
class MockLocalInstance:
    def __init__(self, phone):
        self.phone_number = phone


class MockLocaLList:
    def list(self, limit, area_code, in_locality):
        return [
            MockLocalInstance('+11111111111'),
            MockLocalInstance('+15039253784'),
            MockLocalInstance('+15752222819'),
            MockLocalInstance('+15153053296'),
            MockLocalInstance('+17124819139')
        ]


class MockAvailablePhoneNumberCountryList:
    def __init__(self):
        self.local = MockLocaLList()


class MockClient:
    def available_phone_numbers(self, region):
        return MockAvailablePhoneNumberCountryList()


class PhoneNumberServiceTest(unittest.TestCase):

    @patch('shared_modules.twilio_functions.Client')
    def test_list_phone_numbers_with_no_parameters(self, twilio):
        twilio.return_value = MockClient()

        service = PhoneNumberService()
        result = service.list_available_phone_numbers(5)

        print(result)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], '+11111111111')

    @patch('shared_modules.twilio_functions.Client')
    def test_list_phone_numbers_with_parameters(self, twilio):
        twilio.return_value = MockClient()

        service = PhoneNumberService()
        result = service.list_available_phone_numbers(5, '765', 'chicago')

        print(result)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], '+11111111111')

    # TODO ASH Wait to figure out how to remove numbers before testing in case mocking doesnt work
    # @patch('twilio.rest.api.v2010.account.IncomingPhoneNumberList')
    # def test_create_new_phone_numbers(self, twilio):
    #     twilio.create.return_value = 5
    #
    #     service = PhoneNumberService()
    #     result = service.create_new_phone_number(5, '765', 'chicago')
    #
    #     print(result)
    #     self.assertEqual(len(result), 5)
    #     self.assertEqual(result[0], '+11111111111')
