import miio
import os


def query(capability_type, instance):
    plug = miio.ChuangmiPlug(ip=os.environ['OGONKI_IP'], token=os.environ['OGONKI_TOKEN'])
    if capability_type == "devices.capabilities.on_off":
        return not plug.status().is_on


def action(capability_type, instance, value, relative):
    plug = miio.ChuangmiPlug(ip=os.environ['OGONKI_IP'], token=os.environ['OGONKI_TOKEN'])
    if capability_type == "devices.capabilities.on_off":
        if value:
            plug.on()
        else:
            plug.off()
        return "DONE"
