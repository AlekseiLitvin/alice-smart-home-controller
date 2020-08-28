import os
from miio import ChuangmiPlug
import logging

ip = os.environ['PC_LAMP_IP']
token = os.environ['PC_LAMP_TOKEN']
plug = ChuangmiPlug(ip=ip, token=token, debug=True)


def query(capability_type, instance):
    if capability_type == "devices.capabilities.on_off":
        return plug.status().power


def action(capability_type, instance, value, relative):
    if capability_type == "devices.capabilities.on_off":
        if value:
            plug.on()
        else:
            plug.off()
        return "DONE"
