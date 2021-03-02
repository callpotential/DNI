from Models.BusinessConfig import BusinessConfig
from SharedModules.DatabaseInterface import *
import datetime as dt

def get_business_object_with_business_id(business_id:int):
    sql = "SELECT * FROM BusinessConfig WHERE businessid = " + str(business_id)
    my_result = DatabaseInterface().select(sql)
    business_item = BusinessConfig(my_result[0])

    return business_item


print(BusinessConfig(1,True,False,120,False,"","").__dict__)
