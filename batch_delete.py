__author__ = 'Nathaniel'


import json
import requests

username = "admin"
password = "admin"
aspace_url = "http://localhost:8089"


authenticate = requests.post("{}/users/{}/login?password={}".format(aspace_url, username, password)).json()
token = authenticate["session"]
headers = {"X-ArchivesSpace-Session":token}

agent_ids = ["3"]
for agent_id in agent_ids:
# accession_resource_type
# enumeration_val_id = "273"
    id = {':id' : int(agent_id) }
    request = requests.delete("{}/repositories/{}".format(aspace_url, agent_id), params=id, headers=headers)
    print ("Deleted: " + agent_id)