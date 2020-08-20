import os
from miio import ChuangmiPlug
import logging

ip = os.environ['OGONKI_IP']
token = os.environ['OGONKI_TOKEN']
plug = ChuangmiPlug(ip=ip, token=token, debug=True)
logger = logging.getLogger()


def query(capability_type, instance):
    logger.info("Query device, status {}, capability_type {}".format(plug.status().is_on, capability_type))
    if capability_type == "devices.capabilities.on_off":
        return plug.status().is_on


def action(capability_type, instance, value, relative):
    logger.info(f"Action, value {value}")
    if capability_type == "devices.capabilities.on_off":
        if value:
            plug.on()
        else:
            plug.off()
        return "DONE"
