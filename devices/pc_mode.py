import requests
import os

pc_ip = os.environ['PC_IP']
mode = "work"


def query(capability_type, instance):
    if capability_type == "devices.capabilities.on_off":
        return mode == 'game'


def action(capability_type, instance, value, relative):
    if capability_type == "devices.capabilities.on_off":
        global mode
        mode = 'game' if value else 'work'
        requests.post(f"http://{pc_ip}/mode", data={'mode': mode})
        return "DONE"
