class AssignmentPool:

    def __init__(self, row:dict):
        """This init is for creating an object from a database response"""
        self.poolid = row['poolid']
        self.businessid = row['businessid']
        self.poolphonenumber = row['poolphonenumber']
        self.ttl = row['ttl']
        self.assignedroutingnumber = row['assignedroutingnumber']
        self.sessionid = row['sessionid']
