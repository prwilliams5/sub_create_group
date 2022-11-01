import requests
from morpheuscypher import Cypher

TOKEN = Cypher(morpheus=morpheus, ssl_verify=False).get('secret/pw_api_key:api_key')

SERVER_URL = "cloudkey.corp.gipnetworks.com"
URL = f'https://{SERVER_URL}/api/groups'
HEADERS = {"Authorization": f'BEARER {TOKEN}', "Content-Type": "application/json"}

try:
    GROUP_NAME = morpheus['customOptions']['subgroupname']
except KeyError:
    GROUP_NAME = None

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