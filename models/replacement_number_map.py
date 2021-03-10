from models.phone_number import PhoneNumber
from shared_modules.logger import trace_logging


class ReplacementNumberMap:
    """
    :param replacementphonenumber: This is the phone number from the website that will be dynamically replaced.
    :param routingnumber: This is the phone number that the dynamic number forwards to after a someone calls in.
    :param businessid: This is a unique identifier useful for linking these number combinations to other parts of the database.
    """
    replacementphonenumber: PhoneNumber
    routingnumber: PhoneNumber
    poolid: int

    def __init__(self, row: dict):
        if row is not None:
            self.from_dict(row)

    @trace_logging()
    def from_dict(self, row: dict):
        """This init is for creating an object from a database response"""
        self.replacementphonenumber = PhoneNumber(row['replacementphonenumber'])
        self.routingnumber = PhoneNumber(row['routingnumber'])
        self.poolid = row['poolid']