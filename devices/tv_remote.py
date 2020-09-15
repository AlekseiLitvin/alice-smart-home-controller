import math
import os
import time

import miio

ip = os.environ['REMOTE_IP']
token = os.environ['REMOTE_TOKEN']
remote = miio.ChuangmiIr(ip=ip, token=token)

isOn = False


def query(capability_type, instance):
    global isOn
    if capability_type == "devices.capabilities.on_off":
        return isOn
    else:
        return True


def action(capability_type, instance, value, relative):
    global isOn
    if capability_type == "devices.capabilities.on_off":
        execute_command("power")
        isOn = not isOn
    if capability_type == "devices.capabilities.range":
        if value >= 0:
            execute_command("vol+", value)
        else:
            execute_command("vol-", value)
    if capability_type == "devices.capabilities.mode":
        execute_command("hdmi")
    return "DONE"


def execute_command(name, repeats=1):
    repeats = int(math.fabs(repeats))
    if repeats > 10:
        repeats = 10
    for command in commands:
        if command['name'] == name:
            for _ in range(repeats):
                remote.play_raw(command['code'])
                time.sleep(0.09)


commands = [
    {
        "id": 1,
        "name": "power",
        "description": "Turn on/off",
        "code": "mk1mcwlk0mk5mEsms2mEsmM2m4BFgBkARE1moDKgD+AP4HPgheBl4A/gTuBx4FHzULI5kBx4HHhKeAR4BHgqnMZtNAEVmEAA"
    },
    {
        "id": 2,
        "name": "hdmi",
        "description": "Switch HDMI 3/4",
        "code": "mk1mEwlk0msymEsmszmEsmM3ANIAiZoAjU1nAA/gD+CF4BHgVeAP4IXhC0Az4GXgQeAx4DHhw+BF4A6zCAA="
    },
    {
        "id": 3,
        "name": "vol+",
        "description": "Increase volume",
        "code": "mk1mcwlk0mk4mEsms3mEsmM2AEIAjwCFms1AH8AepsAPIHPgheAP4A7zkAMpkBz4BHgZeBkoHVAteAP4KPgEOCEUxm00mEsm0wAIYBo5hAA="
    },
    {
        "id": 4,
        "name": "vol-",
        "description": "Decrease volume",
        "code": "mk1mcwlk0mk5mEsms2mEsmM2m4BHgEPNZqAP4A/gc+AR4FXgD+CF4HPgIeAP4A/gceAh4BHgEfLJhAA="
    }
]
