import re


class PhoneNumber:

    def __init__(self, phone_number: str = None):
        self.phone_number = phone_number
        self.parse_from_string(phone_number)

    def parse_from_twilio(self, phone_number: str):
        # Remove the leading +
        self.phone_number = phone_number[1:]

    def parse_from_string(self, phone_number: str) -> None:
        # Pull out all the digits and join them together
        matches = re.findall('\\d*', phone_number)
        self.phone_number = ''.join(matches)

    def get_twilio_format(self):
        return '+' + self.phone_number.rjust(11, '0')

    def get_with_dashes(self):
        result = '-'.join([
            self.get_region(),
            self.get_area_code(),
            self.get_central_office_code(),
            self.get_station_number()])
        return result.strip('-')

    def get_region(self) -> str:
        if len(self.phone_number) >= 11:
            return self.phone_number[-11:-10]
        else:
            return ''

    def get_area_code(self) -> str:
        if len(self.phone_number) >= 10:
            return self.phone_number[-10:-7]
        else:
            return ''

    def get_central_office_code(self) -> str:
        if len(self.phone_number) >= 7:
            return self.phone_number[-7:-4]
        else:
            return ''

    def get_station_number(self) -> str:
        if len(self.phone_number) >= 4:
            return self.phone_number[-4:]
        else:
            return ''
