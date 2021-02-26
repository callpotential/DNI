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

    def __init__(self, columns):
        """This init is for creating an object from a database response"""
        self.poolid = columns[0]
        self.businessid = columns[1]
        self.poolphonenumber = columns[2]
        self.ttl = columns[3]
        self.assignedroutingnumber = columns[4]
        self.sessionid = columns[5]