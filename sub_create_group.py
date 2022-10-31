import requests
import sys

SERVER_URL = "10.0.1.21"
TOKEN = sys.argv[1]
URL = f'https://{SERVER_URL}/api/groups'
HEADERS = {"Authorization": f'BEARER {TOKEN}', "Content-Type": "application/json"}
GROUP_NAME = morpheus['customOptions']['subgroupname']

try:
    GROUP_CODE = morpheus['customOptions']['subgroupcode']
except KeyError:
    GROUP_CODE = None

try:
    GROUP_LOCATION = morpheus['customOptions']['subgrouplocation']
except KeyError:
    GROUP_LOCATION = None


def build_payload(gname, gcode, gloc):
    final_payload = {"group": {"name": gname, "code": gcode, "location": gloc}}
    return final_payload


PAYLOAD = build_payload(GROUP_NAME, GROUP_CODE, GROUP_LOCATION)
response = requests.post(URL, json=PAYLOAD, headers=HEADERS, verify=False)
print('Group Added Successfully.')