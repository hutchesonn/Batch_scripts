__author__ = 'Nathaniel'

import requests
import json
import csv
import os
import getpass


#Add OPTION TO PUBLISH FILE VERSIONS?

#This script is used to batch update metadata for digital objects in ASpace using CSV input
username = "admin"
password = "admin"
aspace_url = "http://localhost:8089"

#Prompt for authentication
#aspace_url = raw_input('Aspace backend URL: ')
#aspace_repo = raw_input('Repo number: ')
#username= raw_input('Username: ')
#password = getpass.getpass(prompt='Password: ')

#Authenticate and get a session token
try:
    auth = requests.post(aspace_url+'/users/'+username+'/login?password='+password).json()
except requests.exceptions.RequestException as e:
    print ("Invalid URL, try again")
    exit()
#test authentication
if auth.get("session") == None:
    print ("Wrong username or password! Try Again")
    exit()
else:
#print authentication confirmation
    print ("Hello " + auth["user"]["name"])

session = auth["session"]
headers = {'X-ArchivesSpace-Session':session}

#FILE INPUT / OUTPUT STUFF:
#prompt for input file path
#resource_input_csv = raw_input("Path to input CSV: ")
resource_input_csv = "G:\\Downloads\\scopecontent-2017-05-31.csv"
#prompt for output path
#updated_resource_csv = raw_input("Path to output CSV: ")
updated_resource_csv = "G:\\Downloads\\finished_batch_update.csv"

with open(resource_input_csv,'r') as csvfile, open(updated_resource_csv,'w') as csvout:
    csvin = csv.reader(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
    #next(csvin, None) #ignore header row
    for row in csvin:

        #variables from the input CSV (first column is row[0])
        input_uri = row[0]
        input_identifier = row[1]
        input_scope_content = row[2]
        

        # Use input DO URI to submit a get request for the digital object and store the JSON
        resource_json = requests.get(aspace_url+input_uri,headers=headers).json()

        #Overwrite existing fields with new values from CSV. Comment out any fields you don't want to overwrite
        resource_json['ead_id'] = input_identifier
        
        #Add new notes field
        #notes = []
        #notes.append(json.loads(input_scope_content))
        #resource_json['notes'] = notes
        
        #Append new notes to end of notes
        resource_json['notes'].append(json.loads(input_scope_content))

        #Update a specific existing note
        #resource_notes = resource_json['notes']
        #for i, note in enumerate(resource_notes):
        #    type = note['type']
        #    if type in 'scopecontent':
        #        resource_notes[i] = json.loads(input_scope_content)
        #    else:
        #        continue

        #Form the JSON for the updated digital object
        resource_data = json.dumps(resource_json)

        #Repost the updated digital object
        resource_update = requests.post(aspace_url+input_uri,headers=headers,data=resource_data).json()
        #Capture status response of post request
        update_status = resource_update['status']

        #Print confirmation that archival object was updated. Response should contain any warnings
        print (resource_json['uri'] + ': ' + update_status)

        #add update status to CSV
        row.append(update_status)

        #Lookup the digital object again and capture JSON response for updated digital object
        updated_resource_json = requests.get(aspace_url+input_uri,headers=headers).json()

        #Just stuff all the JSON for the updated object in a cell at the end of the CSV...probably a bad idea
        row.append(updated_resource_json)

        #Write a new csv with all the info from the initial csv + the ArchivesSpace uris for the archival and digital objects
        with open(updated_resource_csv,'a') as csvout:
            writer = csv.writer(csvout, delimiter='|')
            writer.writerow(row)