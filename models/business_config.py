class BusinessConfig:

    def __init__(self, row: dict):
        """This init is for creating an object from a database response"""
        self.businessid = None
        self.active = None
        self.cpmaincustomer = None
        self.defaultttl = None
        self.emailnotifications = None
        self.emailaddress = None
        self.featuretoggle = None

        if row is not None:
            self.from_dict(row)

    def set_businessid(self, businessid: int) -> 'BusinessConfig':
        self.businessid = businessid
        return self

    def set_active(self, active: bool) -> 'BusinessConfig':
        self.active = active
        return self

    def set_cpmaincustomer(self, cpmaincustomer: bool) -> 'BusinessConfig':
        self.cpmaincustomer = cpmaincustomer
        return self

    def set_defaultttl(self, defaultttl: int) -> 'BusinessConfig':
        self.defaultttl = defaultttl
        return self

    def set_emailnotifications(self, emailnotifications: bool) -> 'BusinessConfig':
        self.emailnotifications = emailnotifications
        return self

    def set_emailaddress(self, emailaddress: str) -> 'BusinessConfig':
        self.emailaddress = emailaddress
        return self

    def set_featuretoggle(self, featuretoggle: str) -> 'BusinessConfig':
        self.featuretoggle = featuretoggle
        return self

    def from_dict(self, row: dict):
        """This init is for creating an object from a database response"""
        self.set_businessid(row['businessid'])
        self.set_active(row['active'])
        self.set_cpmaincustomer(row['cpmaincustomer'])
        self.set_defaultttl(row['defaultttl'])
        self.set_emailnotifications(row['emailnotifications'])
        self.set_emailaddress(row['emailaddress'])
        self.set_featuretoggle(row['featuretoggle'])
