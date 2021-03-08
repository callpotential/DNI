class business_config:

    def __init__(self, business_dict:dict):
        self.businessid = business_dict['businessid']
        self.active = business_dict['active']
        self.cpmaincustomer = business_dict['cpmaincustomer']
        self.defaultttl = business_dict['defaultttl']
        self.emailnotifications = business_dict['emailnotifications']
        self.emailaddress = business_dict['emailaddress']
        self.featuretoggle = business_dict['featuretoggle']