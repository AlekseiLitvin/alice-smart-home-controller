import os
from miio import ChuangmiPlug
import logging

ip = os.environ['OGONKI_IP']
token = os.environ['OGONKI_TOKEN']
plug = ChuangmiPlug(ip=ip, token=token, debug=True)
isOn = plug.status().is_on
logger = logging.getLogger()


def query(capability_type, instance):
    global isOn
    logger.info("Query device, status {}, capability_type {}".format(plug.status().is_on, capability_type))
    if capability_type == "devices.capabilities.on_off":
        isOn = not isOn
        return


def action(capability_type, instance, value, relative):
    logger.info(f"Action, value {value}")
    if capability_type == "devices.capabilities.on_off":
        if value:
            plug.on()
        else:
            plug.off()
        return "DONE"
