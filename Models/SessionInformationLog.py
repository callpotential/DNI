class SessionInformationLog:

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
        self.utm_source = row['utm_source']
        self.utm_medium = row['utm_medium']
        self.utm_campaign = row['utm_campaign']
        self.utm_adgroup = row['utm_adgroup']
        self.utm_keyword = row['utm_keyword']
        self.utm_device = row['utm_device']
        self.utm_brandtype = row['utm_brandtype']
        self.utm_content = row['utm_content']
        self.gclsrc = row['gclsrc']
        self.gclid = row['gclid']
        self.fbclid = row['fbclid']
        self.clickid = row['clickid']
