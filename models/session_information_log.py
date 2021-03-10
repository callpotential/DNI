import datetime
from models.phone_number import PhoneNumber
from shared_modules.logger import trace_logging
from shared_modules.proxy_date_time import sql_to_datetime


class SessionInformationLog:

    @trace_logging()
    def __init__(self, row: dict):
        """This is the class that represents the items in the session information log table.
        """
        self.sessionid = None
        self.poolid = None
        self.businessid = None
        self.numberroutedsuccessfully = None
        self.replacementphonenumber = None
        self.routingnumber = None
        self.poolphonenumber = None
        self.callstart = None
        self.callend = None
        self.clicksource = None
        self.url = None
        self.utm_source = None
        self.utm_medium = None
        self.utm_campaign = None
        self.utm_adgroup = None
        self.utm_keyword = None
        self.utm_device = None
        self.utm_brandtype = None
        self.utm_content = None
        self.gclsrc = None
        self.gclid = None
        self.fbclid = None
        self.clickid = None

        if row is not None:
            self.from_dict(row)

    @trace_logging()
    def set_sessionid(self, sessionid: int) -> 'SessionInformationLog':
        self.sessionid = sessionid
        return self

    @trace_logging()
    def set_poolid(self, poolid: int) -> 'SessionInformationLog':
        self.poolid = poolid
        return self

    @trace_logging()
    def set_businessid(self, businessid: int) -> 'SessionInformationLog':
        self.businessid = businessid
        return self

    @trace_logging()
    def set_numberroutedsuccessfully(self, numberroutedsuccessfully: str) -> 'SessionInformationLog':
        self.numberroutedsuccessfully = numberroutedsuccessfully
        return self

    @trace_logging()
    def set_replacementphonenumber(self, replacementphonenumber: PhoneNumber) -> 'SessionInformationLog':
        self.replacementphonenumber = replacementphonenumber
        return self

    @trace_logging()
    def set_routingnumber(self, routingnumber: PhoneNumber) -> 'SessionInformationLog':
        self.routingnumber = routingnumber
        return self

    @trace_logging()
    def set_poolphonenumber(self, poolphonenumber: PhoneNumber) -> 'SessionInformationLog':
        self.poolphonenumber = poolphonenumber
        return self

    @trace_logging()
    def set_callstart(self, callstart: datetime) -> 'SessionInformationLog':
        self.callstart = callstart
        return self

    @trace_logging()
    def set_callend(self, callend: datetime) -> 'SessionInformationLog':
        self.callend = callend
        return self

    @trace_logging()
    def set_clicksource(self, clicksource: str) -> 'SessionInformationLog':
        self.clicksource = clicksource
        return self

    @trace_logging()
    def set_url(self, url: str) -> 'SessionInformationLog':
        self.url = url
        return self

    @trace_logging()
    def set_utm_source(self, utm_source: str) -> 'SessionInformationLog':
        self.utm_source = utm_source
        return self

    @trace_logging()
    def set_utm_medium(self, utm_medium: str) -> 'SessionInformationLog':
        self.utm_medium = utm_medium
        return self

    @trace_logging()
    def set_utm_campaign(self, utm_campaign: str) -> 'SessionInformationLog':
        self.utm_campaign = utm_campaign
        return self

    @trace_logging()
    def set_utm_adgroup(self, utm_adgroup: str) -> 'SessionInformationLog':
        self.utm_adgroup = utm_adgroup
        return self

    @trace_logging()
    def set_utm_keyword(self, utm_keyword: str) -> 'SessionInformationLog':
        self.utm_keyword = utm_keyword
        return self

    @trace_logging()
    def set_utm_device(self, utm_device: str) -> 'SessionInformationLog':
        self.utm_device = utm_device
        return self

    @trace_logging()
    def set_utm_brandtype(self, utm_brandtype: str) -> 'SessionInformationLog':
        self.utm_brandtype = utm_brandtype
        return self

    @trace_logging()
    def set_utm_content(self, utm_content: str) -> 'SessionInformationLog':
        self.utm_content = utm_content
        return self

    @trace_logging()
    def set_gclsrc(self, gclsrc: str) -> 'SessionInformationLog':
        self.gclsrc = gclsrc
        return self

    @trace_logging()
    def set_gclid(self, gclid: str) -> 'SessionInformationLog':
        self.gclid = gclid
        return self

    @trace_logging()
    def set_fbclid(self, fbclid: str) -> 'SessionInformationLog':
        self.fbclid = fbclid
        return self

    @trace_logging()
    def set_clickid(self, clickid: str) -> 'SessionInformationLog':
        self.clickid = clickid
        return self

    @trace_logging()
    def from_dict(self, row: dict):
        """This init is for creating an object from a database response"""
        self.set_sessionid(row['sessionid'])
        self.set_poolid(row['poolid'])
        self.set_businessid(row['businessid'])
        self.set_numberroutedsuccessfully(row['numberroutedsuccessfully'])
        self.set_replacementphonenumber(PhoneNumber(row['replacementphonenumber']))
        self.set_routingnumber(PhoneNumber(row['routingnumber']))
        self.set_poolphonenumber(PhoneNumber(row['poolphonenumber']))
        self.set_callstart(sql_to_datetime(row['callstart']))
        self.set_callend(sql_to_datetime(row['callend']))
        self.set_clicksource(row['clicksource'])
        self.set_url(row['url'])
        self.set_utm_source(row['utm_source'])
        self.set_utm_medium(row['utm_medium'])
        self.set_utm_campaign(row['utm_campaign'])
        self.set_utm_adgroup(row['utm_adgroup'])
        self.set_utm_keyword(row['utm_keyword'])
        self.set_utm_device(row['utm_device'])
        self.set_utm_brandtype(row['utm_brandtype'])
        self.set_utm_content(row['utm_content'])
        self.set_gclsrc(row['gclsrc'])
        self.set_gclid(row['gclid'])
        self.set_fbclid(row['fbclid'])
        self.set_clickid(row['clickid'])
