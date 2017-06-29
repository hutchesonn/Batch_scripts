__author__ = 'Nathaniel'

import json
import requests

username = "admin"
password = "admin"
aspace_url = "http://localhost:8089"
suppressed = "/suppressed"

authenticate = requests.post("{}/users/{}/login?password={}".format(aspace_url, username, password)).json()
token = authenticate["session"]
headers = {"X-ArchivesSpace-Session":token}

enum_val_ids = ["273", "274", "275"]
for enumeration_val_id in enum_val_ids:
    enum_val_id = {':id' : int(enumeration_val_id),
                'suppressed': True }
    requests.post("{}/config/enumeration_values/{}{}".format(aspace_url, enumeration_val_id, suppressed), params=enum_val_id, headers=headers)
    print ("Suppressed: " + enumeration_val_id)