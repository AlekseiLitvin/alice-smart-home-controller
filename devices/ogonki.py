import miio
import os
import logging

from miio import DeviceException


max_retries = 5
retries_count = 0


def query(capability_type, instance):
    plug = miio.ChuangmiPlug(ip=os.environ['OGONKI_IP'], token=os.environ['OGONKI_TOKEN'])
    if capability_type == "devices.capabilities.on_off":
        return not plug.status().is_on


def action(capability_type, instance, value, relative):
    plug = miio.ChuangmiPlug(ip=os.environ['OGONKI_IP'], token=os.environ['OGONKI_TOKEN'])
    global retries_count
    if capability_type == "devices.capabilities.on_off":
        try:
            if value:
                plug.on()
            else:
                plug.off()
            retries_count += 1
            return "DONE"
        except DeviceException:
            logging.info("Device not found, trying again")
            if retries_count < max_retries:
                action(capability_type, instance, value, relative)
