import miio
import os


plug = miio.ChuangmiPlug(ip=os.environ['OGONKI_IP'], token=os.environ['OGONKI_TOKEN'])


def pc_query(capability_type, instance):
    if capability_type == "devices.capabilities.on_off":
        return plug.status().is_on


def pc_action(capability_type, instance, value, relative):
    if capability_type == "devices.capabilities.on_off":
        if value is False:
            plug.on()
        return "DONE"
