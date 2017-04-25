'''

This python script handles the interaction with the Cisco Spark service. It's composed of two 
functions that is called by sensor.py :

isMember - 
function takes token, spaceId and reservationToken as input variables
it returns a boolean representing that a reservation is available or not.

postMsg - 
function takes token, spaceId, msg and img as input variables 
it posts a message (with image) to the relevant space indicating if the reservation has been granted or not.

It was implemented with Python 2.7 running on the Raspberry Pi.


'''




# --- Please note!!  There are no variables to modify in this routine !! -----




# Import libraries used for this function
import requests
import json


def isMember(token, roomId, reservationToken):

    # Get Spark variables - static mapping
    headers = {
        "authorization": "Bearer " + token + '',
        "content-type": "application/json; charset=utf-8"
    }

    query_param = "?roomId=" + roomId
    call = "/memberships" + query_param
    url = "https://api.ciscospark.com/v1" + call  # Spark API base url

    resp = requests.get(url, headers=headers)
    response_json = resp.json()  # Get the json-encoded content from response

    print ("(isMember)Status : ", resp.status_code)  # This is the http request status

    member = response_json["items"]

    membership = []

    state = False

    for item in range(len(member)):
        membership.append(member[item]['personEmail'])
        if member[item]['personEmail'] == reservationToken:
            state = True

    print ('\nToken Requested: ', reservationToken)
    print ('Tokens in reservation list: \n', membership, '\n\n')

    return (state)


def postMsg(token, roomId, msg, img):

    # Get Spark variables - static mapping
    headers = {
        "authorization": "Bearer " + token + '',
        "content-type": "application/json"
    }

    # Post a message to a specific room identified by roomId
    call = "/messages"
    post_url = "https://api.ciscospark.com/v1" + call  # Spark API base url

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

    resp = requests.post(post_url, json.dumps(path_data), headers=headers)
    response_json = resp.json()  # Get the json-encoded content from response

    print ("(postmsg)Status: ", resp.status_code)  # This is the http request status




