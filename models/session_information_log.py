import datetime
from models.phone_number import PhoneNumber
from shared_modules.logger import trace_logging
from shared_modules.proxy_date_time import ProxyDateTime


class SessionInformationLog:
    sessionid: int
    poolid: int
    businessid: int
    numberroutedsuccessfully: str
    replacementphonenumber: PhoneNumber
    routingnumber: PhoneNumber
    poolphonenumber: PhoneNumber
    callstart: datetime
    callend: datetime
    clicksource: str
    url: str
    utm_source: str
    utm_medium: str
    utm_campaign: str
    utm_adgroup: str
    utm_keyword: str
    utm_device: str
    utm_brandtype: str
    utm_content: str
    gclsrc: str
    gclid: str
    fbclid: str
    clickid: str

    @trace_logging()
    def __init__(self, row: dict):
        """This is the class that represents the items in the session information log table.
        """
        if row is not None:
            self.from_dict(row)

    @trace_logging()
    def from_dict(self, row: dict):
        """This init is for creating an object from a database response"""
        self.sessionid = row['sessionid']
        self.poolid = row['poolid']
        self.businessid = row['businessid']
        self.numberroutedsuccessfully = row['numberroutedsuccessfully']
        self.replacementphonenumber = PhoneNumber(row['replacementphonenumber'])
        self.routingnumber = PhoneNumber(row['routingnumber'])
        self.poolphonenumber = PhoneNumber(row['poolphonenumber'])
        self.callstart = row['callstart']
        self.callend = row['callend']
        self.clicksource = row['clicksource']
        self.url = row['url']
        self.utm_source = row['utm_source']
        self.utm_medium = row['utm_medium']
        self.utm_campaign = row['utm_campaign']
        self.utm_adgroup = row['utm_adgroup']
        self.utm_keyword = row['utm_keyword']
        self.utm_device = row['utm_device']
        self.utm_brandtype = row['utm_brandtype']
        self.utm_content = row['utm_content']
        self.gclsrc = row['gclsrc']
        self.gclid = row['gclid']
        self.fbclid = row['fbclid']
        self.clickid = row['clickid']
