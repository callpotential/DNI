class ReplacementNumberMap:

    def __init__(self, map_dict:dict):
        """
        :param replacementphonenumber: This is the phone number from the website that will be dynamically replaced.
        :param routingnumber: This is the phone number that the dynamic number forwards to after a someone calls in.
        :param businessid: This is a unique identifier useful for linking these number combinations to other parts of the database.
        """
        self.replacementphonenumber = map_dict['replacementphonenumber']
        self.routingnumber = map_dict['routingnumber']
        self.poolid = map_dict['poolid']