class SessionInformationLog:
    def __init__(self,
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
        self.ttl = ttl
        self.callstart = callstart
        self.callend = callend
        self.clickid = clickid
        self.clicksource = clicksource
        self.url = url
