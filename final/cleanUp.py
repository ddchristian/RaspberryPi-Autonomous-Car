'''

The cleanUp.py script is used to save your working code to you Spark space and delete the code from
your Raspberry Pi.

Implemented with Python 2.7

'''


# Import libraries used for this function
import subprocess
import os

# --- Modify variables below based on your group -----

# Copy the value of 'token = ' from notes.txt
# If the value is not copied to notes.txt yet then get new token from https://developer.ciscospark.com/apps.html
token = ''

# Copy the value of 'roomId = ' from notes.txt
# If the value is not copied to notes.txt yet then run function roomId.py
roomId = ''


# --- Modify variables above based on your group -----


# -- Or get variables from notes.txt -----
f = open('/home/pi/code/notes.txt', 'r')
f.readline()
for line in f:
        newline=line.split("=")
        if newline[0].strip() == "Spark Access Token" :
            token = newline[1].strip()
        else :
            if newline[0].strip() =="roomId (for team space)" :
                roomId = newline[1].strip()
                break

print "token is:", token
print "roomId is:", roomId

# -- Clean up artifacts from repository and zip file to home directory ---
subprocess.call(["pwd"])
print ("Changing to ~/code ...")
os.chdir("/home/pi/code")
subprocess.call(["pwd"])
print ("Removing repository artifacts ...")
subprocess.call(["rm", "-rf", ".git"])
subprocess.call(["rm", "-rf", ".idea"])
print ("Chaning to home directory ...")
os.chdir("/home/pi")
subprocess.call(["pwd"])
print ("Creating zip file of ~code directory... ")
subprocess.call(["zip", "-r", "autonomous.zip", "./code/"])

# -- Setup cURL variables for call to upload zip file to Spark space.
files = "files=@/home/pi/autonomous.zip"

authStr = "Authorization: Bearer %s" %(token)

roomIdStr = "roomId=%s" %(roomId)

call = "https://api.ciscospark.com/v1/messages"

msg = "text=Your code is posted above. Thank you for coding with us today. You can access the repository from GitHub at https://github.com/ddchristian/RaspberryPi-Autonomous-Car"


print (files)
print (authStr)
print (roomIdStr)
print (call)
print (msg)

# --Upload your zip file to your Spark space
subprocess.call(["curl", "-F", files, "--request", "POST", "-H", authStr, "-F", roomIdStr, call, "-F", msg])
