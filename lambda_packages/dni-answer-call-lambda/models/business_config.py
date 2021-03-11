from shared_modules.logger import trace_logging


class BusinessConfig:
    businessid: int
    active: bool
    cpmaincustomer: bool
    defaultttl: int
    emailnotifications: bool
    emailaddress: str
    featuretoggle: str

    def __init__(self, row: dict = None):
        """This init is for creating an object from a database response"""
        if row is not None:
            self.from_dict(row)

    @trace_logging()
    def from_dict(self, row: dict):
        """This init is for creating an object from a database response"""
        self.businessid = row['businessid']
        self.active = row['active']
        self.cpmaincustomer = row['cpmaincustomer']
        self.defaultttl = row['defaultttl']
        self.emailnotifications = row['emailnotifications']
        self.emailaddress = row['emailaddress']
        self.featuretoggle = row['featuretoggle']
