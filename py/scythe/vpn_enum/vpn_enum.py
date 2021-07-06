import uuid
import tunnelblick
g_client = None

CATEGORY_WORKER = 4
VPN_ENUM_MODULE_ID = uuid.UUID('7794d660-ddc9-11eb-b5dd-a93b1cb35228')


def init(client, **kwargs):
    global g_client
    g_client = client
    return True

def run(message,  **kwargs):
    return tunnelblick.auto_connect()

def getinfo():
    return {"type": CATEGORY_WORKER, "version": {"major": 1, "minor": 0}, "id": VPN_ENUM_MODULE_ID}


def deinit(**kwargs):
    return True
