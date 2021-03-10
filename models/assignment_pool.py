import datetime
from models.phone_number import PhoneNumber
from shared_modules.logger import trace_logging
from shared_modules.proxy_date_time import sql_to_datetime


class AssignmentPool:
    poolid: int
    businessid: int
    poolphonenumber: PhoneNumber
    ttl: datetime
    assignedroutingnumber: PhoneNumber
    sessionid: int

    def __init__(self, row: dict = None):
        """This init is for creating an object from a database response"""
        if row is not None:
            self.from_dict(row)

    @trace_logging()
    def from_dict(self, row: dict):
        """This init is for creating an object from a database response"""
        self.poolid = row['poolid']
        self.businessid = row['businessid']
        self.poolphonenumber = PhoneNumber(row['poolphonenumber'])
        self.ttl = sql_to_datetime(row['ttl'])
        self.assignedroutingnumber = PhoneNumber(row['assignedroutingnumber'])
        self.sessionid = row['sessionid']
