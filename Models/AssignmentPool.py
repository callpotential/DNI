class AssignmentPool:
    def __init__(self,
                poolid:int,
                businessid:int,
                poolphonenumber:str,
                ttl:int,
                assignedroutingnumber:str,
                sessionid:int):

        self.poolid = poolid
        self.businessid = businessid
        self.poolphonenumber = poolphonenumber
        self.ttl = ttl
        self.assignedroutingnumber = assignedroutingnumber
        self.sessionid = sessionid