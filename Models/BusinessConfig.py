class BusinessConfig:
    def build(self,
                businessid:int,
                active:bool,
                cpmaincustomer:bool,
                defaultttl:int,
                emailnotifications:bool,
                emailaddress:str,
                featuretoggle:str):
        self.businessid = businessid
        self.active = active
        self.cpmaincustomer = cpmaincustomer
        self.defaultttl = defaultttl
        self.emailnotifications = emailnotifications
        self.emailaddress = emailaddress
        self.featuretoggle = featuretoggle

    def __init__(self, business_dict:dict):
        self.businessid = business_dict['businessid']
        self.active = business_dict['active']
        self.cpmaincustomer = business_dict['cpmaincustomer']
        self.defaultttl = business_dict['defaultttl']
        self.emailnotifications = business_dict['emailnotifications']
        self.emailaddress = business_dict['emailaddress']
        self.featuretoggle = business_dict['featuretoggle']