import requests
import os
import time
from devices import pc_mode


pc_ip = os.environ['PC_IP']


def query(capability_type, instance):
    return True


def action(capability_type, instance, value, relative):
    if capability_type == "devices.capabilities.on_off":
        requests.post(f"http://{pc_ip}:8000/mode", data={'mode': 'work'})
        pc_mode.mode = "work"
        time.sleep(2)
        requests.post(f"http://{pc_ip}:8000/mode", data={'mode': 'sleep'})
        return "DONE"
