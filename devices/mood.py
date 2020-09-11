import os

import miio

ip = os.environ['REMOTE_IP']
token = os.environ['REMOTE_TOKEN']
remote = miio.ChuangmiIr(ip=ip, token=token)

isOn = False


def query(capability_type, instance):
    return isOn


def action(capability_type, instance, value, relative):
    global isOn
    if capability_type == "devices.capabilities.on_off":
        isOn = not isOn
        execute_command("power")
    return "DONE"


def execute_command(name):
    for command in commands:
        if command['name'] == name:
            remote.play_raw(command['code'])


commands = [
    {
        "id": 5,
        "name": "power",
        "description": "Turn on/off",
        "code": "nMwmUwlk0mk2mEsms4ADKaAD+AP4A/gD7MZtNQCPAI8AjweSmM2m4DXAr+APgVZhX8Bx4MngEeD/4P7Ae/LJhAA="
    }
]
