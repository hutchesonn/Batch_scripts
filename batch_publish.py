__author__ = 'Nathaniel'

import requests
import json
import csv
import os
import getpass

# Add OPTION TO PUBLISH FILE VERSIONS?

# This script is used to batch update metadata for digital objects in ASpace using CSV input
username = "admin"
password = "admin"
aspace_url = "http://localhost:8089"
repo = "/repositories/2/resources/"
published = "/publish"

# Prompt for authentication
# aspace_url = raw_input('Aspace backend URL: ')
# aspace_repo = raw_input('Repo number: ')
# username= raw_input('Username: ')
# password = getpass.getpass(prompt='Password: ')

# Authenticate and get a session token
try:
    auth = requests.post(aspace_url + '/users/' + username + '/login?password=' + password).json()
except requests.exceptions.RequestException as e:
    print ("Invalid URL, try again")
    exit()
# test authentication
if auth.get("session") == None:
    print ("Wrong username or password! Try Again")
    exit()
else:
    # print authentication confirmation
    print ("Hello " + auth["user"]["name"])

session = auth["session"]
headers = {'X-ArchivesSpace-Session': session}

# FILE INPUT / OUTPUT STUFF:
# prompt for input file path
# resource_input_csv = raw_input("Path to input CSV: ")
resource_input_csv = "G:\\Downloads\\batch_updates\\bioghist_2017_06_01.csv"
# prompt for output path
# updated_resource_csv = raw_input("Path to output CSV: ")
updated_resource_csv = "G:\\Downloads\\finished_batch_update.csv"

with open(resource_input_csv, 'r', encoding='utf-8') as csvfile, open(updated_resource_csv, 'w') as csvout:
    csvin = csv.reader(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
    # next(csvin, None) #ignore header row
    for row in csvin:

        # variables from the input CSV (first column is row[0])
        input_uri = row[0]
        requests.post(aspace_url + repo + input_uri + published, headers=headers)
        print ("Published: "+input_uri)