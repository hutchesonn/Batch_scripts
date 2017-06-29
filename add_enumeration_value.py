import json
import requests

username = "admin"
password = "admin"
aspace_url = "http://localhost:8089"

authenticate = requests.post("{}/users/{}/login?password={}".format(aspace_url, username, password)).json()
token = authenticate["session"]
headers = {"X-ArchivesSpace-Session":token}

# accession_resource_type
enumeration_id = "35"
new_values = ["received"]
enumeration = requests.get("{}/config/enumerations/{}".format(aspace_url, enumeration_id), headers=headers).json()
enumeration["values"].extend(new_values)

requests.post("{}/config/enumerations/{}".format(aspace_url, enumeration_id), data=json.dumps(enumeration), headers=headers)
