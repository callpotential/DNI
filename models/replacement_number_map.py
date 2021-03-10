from models.phone_number import PhoneNumber


class ReplacementNumberMap:

    def __init__(self, row: dict):
        """
        :param replacementphonenumber: This is the phone number from the website that will be dynamically replaced.
        :param routingnumber: This is the phone number that the dynamic number forwards to after a someone calls in.
        :param businessid: This is a unique identifier useful for linking these number combinations to other parts of the database.
        """
        self.replacementphonenumber = None
        self.routingnumber = None
        self.poolid = None

        if row is not None:
            self.from_dict(row)

    def set_replacementphonenumber(self, replacementphonenumber: PhoneNumber) -> 'ReplacementNumberMap':
        self.replacementphonenumber = replacementphonenumber
        return self

    def set_routingnumber(self, routingnumber: PhoneNumber) -> 'ReplacementNumberMap':
        self.routingnumber = routingnumber
        return self

    def set_poolid(self, poolid: int) -> 'ReplacementNumberMap':
        self.poolid = poolid
        return self

    def from_dict(self, row: dict):
        """This init is for creating an object from a database response"""
        self.set_replacementphonenumber(PhoneNumber(row['replacementphonenumber']))
        self.set_routingnumber(PhoneNumber(row['routingnumber']))
        self.set_poolid(row['poolid'])