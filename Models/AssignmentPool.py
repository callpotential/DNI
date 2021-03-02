class AssignmentPool:
    def build(self,
                poolid:int,
                businessid:int,
                poolphonenumber:str,
                ttl: str,
                assignedroutingnumber:str,
                sessionid:int):

        self.poolid = poolid
        self.businessid = businessid
        self.poolphonenumber = poolphonenumber
        self.ttl = ttl
        self.assignedroutingnumber = assignedroutingnumber
        self.sessionid = sessionid

    def __init__(self, row:dict):
        """This init is for creating an object from a database response"""
        self.poolid = row['poolid']
        self.businessid = row['businessid']
        self.poolphonenumber = row['poolphonenumber']
        self.ttl = row['ttl']
        self.assignedroutingnumber = row['assignedroutingnumber']
        self.sessionid = row['sessionid']
