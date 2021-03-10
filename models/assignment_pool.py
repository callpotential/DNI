import datetime

from models.phone_number import PhoneNumber
from shared_modules.proxy_date_time import sql_to_datetime


class AssignmentPool:

    def __init__(self, row: dict = None):
        """This init is for creating an object from a database response"""
        self.poolid = None
        self.businessid = None
        self.poolphonenumber = None
        self.ttl = None
        self.assignedroutingnumber = None
        self.sessionid = None

        if row is not None:
            self.from_dict(row)

    def set_poolid(self, poolid: int) -> 'AssignmentPool':
        self.poolid = poolid
        return self

    def set_businessid(self, businessid: int) -> 'AssignmentPool':
        self.businessid = businessid
        return self

    def set_poolphonenumber(self, poolphonenumber: PhoneNumber) -> 'AssignmentPool':
        self.poolphonenumber = poolphonenumber
        return self

    def set_ttl(self, ttl: datetime) -> 'AssignmentPool':
        self.ttl = ttl
        return self

    def set_assignedroutingnumber(self, assignedroutingnumber: PhoneNumber) -> 'AssignmentPool':
        self.assignedroutingnumber = assignedroutingnumber
        return self

    def set_sessionid(self, sessionid: int) -> 'AssignmentPool':
        self.sessionid = sessionid
        return self

    def from_dict(self, row: dict):
        """This init is for creating an object from a database response"""
        self.set_poolid(row['poolid'])
        self.set_businessid(row['businessid'])
        self.set_poolphonenumber(PhoneNumber(row['poolphonenumber']))
        self.set_ttl(sql_to_datetime(row['ttl']))
        self.set_assignedroutingnumber(PhoneNumber(row['assignedroutingnumber']))
        self.set_sessionid(row['sessionid'])
