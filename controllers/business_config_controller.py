from models.business_config import BusinessConfig
from shared_modules.database_interface import *
import datetime as dt

from shared_modules.logger import trace_logging


@trace_logging()
def get_business_object_with_business_id(business_id:int):
    sql = "SELECT * FROM business_config WHERE businessid = " + str(business_id)
    my_result = DatabaseInterface().select(sql)
    business_item = BusinessConfig(my_result[0])

    return business_item
