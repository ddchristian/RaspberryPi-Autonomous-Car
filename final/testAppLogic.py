'''

This module is intended to test the application logic without a Raspberry Pi. Since the Raspberry Pi acts as a sensor
providing on or off state to the application that state can be set statically using the Led_status variable.
All calls to Cisco Spark will still be called.

This project was conceived as a means to introduce coding, IoT sensors and cloud applications to high school students.
The project focuses on autonomous vehicles using the Raspberry Pi to simulate a sensor and the and the Cisco Spark 
service to simulate a cloud based application server.

The use case was conceived from research done by University of Texas, Austin published in this video:
https://www.youtube.com/watch?v=4pbAI40dK0A

This project's objective is to simulate the implementation of an Autonomous Intersection Management Traffic 
Control System.

This project was implemented with Python 2.7 running on a MAC OSX. It can also run using Python 3.5

This is the main function. It imports the follwoing functions from spark.py:
isMember - determines if a specified user is a member of the space(room). This grants a reservation to enter the intersection.

postmsg - post the message an image in the Spark space. This is the result of the reservation being granted or not.

'''




# --- Modify variables below based on your group -----

# Use variables from notes.txt
# roomId is the same as spaceId
# reservationToken is the email address for one of the users on your space. This is what the system use to grant you
# a reservation.
# To test the case where the system will deny a reservation use any email that is not part of the space.
token = ''

roomId = ''

reservationToken = ''


# --- Modify variables above based on your group -----




#  ----------------------------------------------------------------
#
#  This part of the code set's some additional variables required
#  for the Spark application as well as importing the code that
#  interacts with the Spark application.
#
#  ----------------------------------------------------------------



# import functions used to interact with the Spark application
# spark.py should be in the same directory where this function is called
from spark import isMember, postMsg

# Cisco Spark spaces used to be called rooms. The API's are implemented using the room terminology.
# A Cisco Spark Room is the same as a  Spark Space.


# Reference images to visually represent the resulting reservation
img_go = 'http://www.clker.com/cliparts/z/r/p/I/x/a/green-led-on-md.png'

img_stop = 'http://www.clker.com/cliparts/5/I/2/4/C/X/red-led-off-md.png'



#  ----------------------------------------------------------------
#
#  This part of the code implements the logic. It takes the
#  imput from the sensor as well as input from the Spark space,
#  runs the application logic output the result back to end user
#  application (Spark space).
#
#  ----------------------------------------------------------------


		
Led_status = 0

#Led_status = 1


if Led_status == 1:
    print ('LED Off: On lookout for next intersection...')


else:

    print ('LED On: Vehicle at intersection...')

    if isMember(token, roomId, reservationToken):
        print ('Reservation Granted')
        msg = 'Reservation Granted. Proceed through intersection'
        postMsg(token, roomId, msg, img_go)
        print ('call postmsg. See message posted in your Spark Space')

    else:

        print ('Reservation Denied')
        msg = 'Reservation Denied. Slow down and request timeslot again'
        postMsg(token, roomId, msg, img_stop)
        print ('call postmsg. See message posted in your Spark Space')


