import os

import miio

ip = os.environ['TV_IP']
token = os.environ['TV_TOKEN']
remote = miio.ChuangmiIr(ip=ip, token=token)


def action(capability_type, instance, value, relative):
    if capability_type == "devices.capabilities.on_off":
        execute_command("power")
    if capability_type == "devices.capabilities.range":
        if value >= 0:
            execute_command("vol+", value)
        else:
            execute_command("vol-", value)
    if capability_type == "devices.capabilities.toggle":
        execute_command("hdmi")


def execute_command(name, repeats=1):
    for command in commands:
        if command['name'] == name:
            for _ in range(repeats):
                remote.play_raw(command['code'])


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
