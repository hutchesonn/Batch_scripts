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

enum_val_ids = ["904", "913", "907", "916", "917", "295", "296", "297", "298", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "1341", "1342", "1343", "1340", "348", "231", "232", "234", "235", "241", "243", "237", "238", "239", "363", "358", "359", "360", "362", "273", "276", "279", "280", "281", "282"]
for enumeration_val_id in enum_val_ids:
    enum_val_id = {':id' : int(enumeration_val_id),
                'suppressed': True }
    requests.post("{}/config/enumeration_values/{}{}".format(aspace_url, enumeration_val_id, suppressed), params=enum_val_id, headers=headers)
    print ("Suppressed: " + enumeration_val_id)