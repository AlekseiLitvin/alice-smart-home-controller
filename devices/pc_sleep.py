import requests
import os

from requests import Timeout

pc_ip = os.environ['PC_IP']


def query(capability_type, instance):
    if capability_type == "devices.capabilities.on_off":
        try:
            resp = requests.get(f"http://{pc_ip}]/healthcheck", timeout=0.2)
            return resp.status_code == 200
        except Timeout:
            return False


def action(capability_type, instance, value, relative):
    if capability_type == "devices.capabilities.on_off":
        requests.post(f"http://{pc_ip}:8000/mode", data={'mode': 'sleep'})
        return "DONE"
