from urllib import parse

from shared_modules.logger import trace_logging

PARSING_TEMPLATE = {
            "utm_source": "NULL",
            "utm_medium": "NULL",
            "utm_campaign": "NULL",
            "utm_adgroup": "NULL",
            "utm_keyword": "NULL",
            "utm_device": "NULL",
            "utm_brandtype": "NULL",
            "utm_content": "NULL",
            "gclsrc": "NULL",
            "gclid": "NULL",
            "fbclid": "NULL",
            "twclid": "NULL"
        }

class ParsedUrl:
    def __init__(self, url):
        parsing_template = PARSING_TEMPLATE
        parse.urlsplit(url)
        parse.parse_qs(parse.urlsplit(url).query)
        params = dict(parse.parse_qsl(parse.urlsplit(url).query))

        for key in params.keys():
            parsing_template[key] = params[key]
        self.url = url
        self.utm_source = parsing_template['utm_source']
        self.utm_medium = parsing_template['utm_medium']
        self.utm_campaign = parsing_template['utm_campaign']
        self.utm_adgroup = parsing_template['utm_adgroup']
        self.utm_keyword = parsing_template['utm_keyword']
        self.utm_device = parsing_template['utm_device']
        self.utm_brandtype = parsing_template['utm_brandtype']
        self.utm_content = parsing_template['utm_content']
        self.gclsrc = parsing_template['gclsrc']
        self.gclid = parsing_template['gclid']
        self.fbclid = parsing_template['fbclid']
        self.twclid = parsing_template['twclid']
        self.clickid = self.get_click_id()

    @trace_logging()
    def get_click_id(self):
        if self.gclid != "NULL":
            return self.gclid
        elif self.fbclid != "NULL":
            return self.fbclid
        elif self.twclid != "NULL":
            return self.twclid
        else:
            return "NULL"



