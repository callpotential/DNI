class SessionInformationLog:
    def build(self,
        sessionid:int,
        poolid:int,
        businessid:int,
        numberroutedsuccessfully:bool,
        replacementphonenumber:str,
        routingnumber:str,
        poolphonenumber:str,
        ttl:str,
        callstart:str,
        callend:str,
        clickid:str,
        clicksource:str,
        url:str):
        """This is the class that represents the items in the session information log table.
        """
        self.sessionid = sessionid
        self.poolid = poolid
        self.businessid = businessid
        self.numberroutedsuccessfully = numberroutedsuccessfully
        self.replacementphonenumber = replacementphonenumber
        self.routingnumber = routingnumber
        self.poolphonenumber = poolphonenumber
        self.callstart = callstart
        self.callend = callend
        self.clickid = clickid
        self.clicksource = clicksource
        self.url = url

    def __init__(self,row:dict):
        """This is the class that represents the items in the session information log table.
        """
        self.sessionid = row['sessionid']
        self.poolid = row['poolid']
        self.businessid = row['businessid']
        self.numberroutedsuccessfully = row['numberroutedsuccessfully']
        self.replacementphonenumber = row['replacementphonenumber']
        self.routingnumber = row['routingnumber']
        self.poolphonenumber = row['poolphonenumber']
        self.callstart = row['callstart']
        self.callend = row['callend']
        self.clickid = row['clickid']
        self.clicksource = row['clicksource']
        self.url = row['url']