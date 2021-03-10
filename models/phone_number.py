import re
from shared_modules.logger import trace_logging


class PhoneNumber:

    def __init__(self, phone_number: str = None):
        self.phone_number = phone_number
        if phone_number is not None:
            self.parse_from_string(phone_number)

    @trace_logging()
    def parse_from_twilio(self, phone_number: str):
        # Remove the leading +
        self.phone_number = phone_number[1:]

    @trace_logging()
    def parse_from_string(self, phone_number: str) -> None:
        # Pull out all the digits and join them together
        matches = re.findall('\\d*', phone_number)
        self.phone_number = ''.join(matches)

    @trace_logging()
    def get_twilio_format(self):
        return '+' + self.phone_number.rjust(11, '0')

    @trace_logging()
    def get_with_dashes(self):
        result = '-'.join([
            self.get_region(),
            self.get_area_code(),
            self.get_central_office_code(),
            self.get_station_number()])
        return result.strip('-')

    @trace_logging()
    def get_region(self) -> str:
        if len(self.phone_number) >= 11:
            return self.phone_number[-11:-10]
        else:
            return ''

    @trace_logging()
    def get_area_code(self) -> str:
        if len(self.phone_number) >= 10:
            return self.phone_number[-10:-7]
        else:
            return ''

    @trace_logging()
    def get_central_office_code(self) -> str:
        if len(self.phone_number) >= 7:
            return self.phone_number[-7:-4]
        else:
            return ''

    @trace_logging()
    def get_station_number(self) -> str:
        if len(self.phone_number) >= 4:
            return self.phone_number[-4:]
        else:
            return ''
