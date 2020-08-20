import os
from miio import ChuangmiPlug
import logging


plug = ChuangmiPlug(ip=os.environ['OGONKI_IP'], token=os.environ['OGONKI_TOKEN'], debug=True)
logger = logging.getLogger()


def query(capability_type, instance):
    logger.info("Query device, status {}, capability_type {}".format(plug.status().is_on, capability_type))
    if capability_type == "devices.capabilities.on_off":
        return not plug.status().is_on


def action(capability_type, instance, value, relative):
    logger.info("Action, value {}".format(value))
    if capability_type == "devices.capabilities.on_off":
        if value:
            plug.on()
        else:
            plug.off()
        return "DONE"
