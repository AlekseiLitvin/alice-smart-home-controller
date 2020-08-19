import miio
import os


plug = miio.ChuangmiPlug(ip=os.environ['OGONKI_IP'], token=os.environ['OGONKI_TOKEN'])


def query(capability_type, instance):
    if capability_type == "devices.capabilities.on_off":
        return not plug.status().is_on


def action(capability_type, instance, value, relative):
    if capability_type == "devices.capabilities.on_off":
        if value:
            plug.on()
        else:
            plug.off()
        return "DONE"
