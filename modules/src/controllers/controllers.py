from ..services.services import getOsInfo

def returnInfo():
    os_name = getOsInfo()
    return os_name
