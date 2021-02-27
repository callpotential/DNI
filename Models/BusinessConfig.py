class BusinessConfig:
    def __init__(self,
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
