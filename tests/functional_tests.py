from models.phone_number import PhoneNumber
from services.number_assignment.number_assignment_service import get_assignment_pool_number

get_assignment_pool_number("https://www.cubesmart.com/illinois-self-storage/chicago-self-storage/?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2Bsmart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB",
                           PhoneNumber("234-123-4323"))

