'''

The roomId.py function is called to determine what spaces (rooms) I belong to.

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
# If the value is not copied to notes.txt yet then get new token from https://developer.ciscospark.com/apps.html
token = ''

# --- Modify variables above based on your group -----



# Get Spark variables - static mapping
headers = {
    "authorization": "Bearer " + token + '',
    "content-type": "application/json; charset=utf-8"
}


call = "rooms"  # Spark API call
url = "https://api.ciscospark.com/v1/" + call  # Spark API base url

# Just print all our call objects
print ("Let's see all the setup paramaters before making our API call:")
print ("Headers are: ")
print (headers)
print ("API call is: ")
print (call)
print ("API url is: ")
print (url)

resp = requests.get(url, headers=headers)
response_json = resp.json()  # Get the json-encoded content from response

print ("\n")
print ("Status: ", resp.status_code)  # This is the http request status

print ("\n\nLet's see all of the JSON output from our API call:")
print (json.dumps(response_json, indent=4))  # Convert "response_json" object to a JSON formatted string and print it out

# Let's get the API response into a variable so that we can iterate and print it out more legibly
rooms = response_json["items"]

print ("\n\nThese are all the spaces you belong to:")
for item in range(len(rooms)):
    print (rooms[item]['title'] + '\n' + rooms[item]['id'] + '\n')


