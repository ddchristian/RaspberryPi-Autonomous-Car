'''

The postMsg.py function is called to post messages to your Spark space (room) identified by roomId.

It is used with other functions as part of an Autonomous Driving Coding exercise.

It uses the Raspberry Pi simulating a sensor at a traffic intersection and
using the Cisco Spark service simulating an application server.

Implemented with Python 2.7

'''

# Import libraries used for this function
import requests
import json


# --- Modify variables below based on your group -----

# Copy the value of 'token = ' from notes.txt
token = ''

# Use roomId from notes.txt
roomId = ''

# --- Modify variables above based on your group -----



# Get Spark variables - static mapping
headers = {
    "authorization": "Bearer " + token + '',
    "content-type": "application/json"
}

call = "/messages"
post_url = "https://api.ciscospark.com/v1" + call  # Spark API base url

# Just print all our call objects
print ("Let's see all the setup paramaters before making our API call:")
print ("Headers are: ")
print (headers)
print ("API call is: ")
print (call)
print ("API url is: ")
print (post_url)


msg = raw_input('\n\n=> Enter the message you would like to post to the space.....: ')
img = raw_input('\n\n=> Enter the image URL you would like to post to the space or Enter for no image.....: ')

img = img.rstrip()

if img != '':

    file_url = img

    path_data = {
        "roomId": roomId,
        "file": file_url,
        "text": msg
    }

else:

    path_data = {
        "roomId": roomId,
        "text": msg
    }

print ('\nBefore post... path data is...: ', path_data, '\n')

resp = requests.post(post_url, json.dumps(path_data), headers=headers)
response_json = resp.json()  # Get the json-encoded content from response

print ("\n")
print ("Status: ", resp.status_code)  # This is the http request status
print (json.dumps(response_json, indent=4))  # Convert "response_json" object to a JSON formatted string and print it out

print ('\n\nSee message posted in your Spark Space')

