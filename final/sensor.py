'''

This is the main module for this project.

The project was conceived as a means to introduce coding, IoT sensors and cloud applications to high school students.
It focuses on autonomous vehicles using the Raspberry Pi to simulate a sensor and Cisco Spark service to simulate 
a cloud based application server.

The specific use case was conceived from research done by University of Texas, Austin published in this video:
https://www.youtube.com/watch?v=4pbAI40dK0A

The objective of the project is to simulate the implementation of an Autonomous Intersection Management Traffic 
Control System.

The Raspberry Pi was build with a sensor kit from Sunfounder:
https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-2-controlling-an-led-by-a-button-super-kit-for-raspberrypi.html

The source code for the Sunfounder Raspberry was modified and integrated with the Cisco Spark API's and application 
logic. The original source code can be found at:
https://github.com/sunfounder/Sunfounder_SuperKit_Python_code_for_RaspberryPi/blob/master/02_btnAndLed.py

The project was implemented with Python 2.7 running on the Raspberry Pi.

This module imports the follwoing functions from spark.py :

isMember - determines if a specified user is a member of the space(room). This grants a reservation to enter the intersection.

postMsg - post the message an image in the Spark space(room). This is the result of the reservation being granted or not.

'''




# --- Modify variables below based on your group -----

# Use variables from notes.txt
# reservationToken is the email address for one of the users on your space. This is what the system use to grant you
# a reservation.
# To test the case where the system will deny a reservation use any email that is not part of the space.
token = ''

roomId = ''

reservationToken = ''


# --- Modify variables above based on your group -----





#  ----------------------------------------------------------------
#
#  NOTE: Do not modify any of this code below this line !!!
#
#  ----------------------------------------------------------------







#  ----------------------------------------------------------------
#
#  This part of the code set's up the sensor (Raspberry Pi) which
#  is simulating the vehicle's arrival at the intersection.
#
#  ----------------------------------------------------------------

import RPi.GPIO as GPIO

LedPin = 11  # pin11 --- led
BtnPin = 12  # pin12 --- button

Led_status = 1


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)  # Set LedPin's mode is output
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.output(LedPin, GPIO.HIGH)  # Set LedPin high(+3.3V) to off led


def swLed(ev=None):
    global Led_status
    Led_status = not Led_status
    GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
    if Led_status == 1:
        print ('led off...')
    else:
        print ('...led on')


def loop():
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed)  # wait for falling
    while True:
        pass  # Don't do anything


def destroy():
    GPIO.output(LedPin, GPIO.HIGH)  # led off
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here


    setup()
    try:

        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.

        GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
        if Led_status == 1:
            print ('LED Off: On lookout for next intersection...')
            destroy()


        else:
            print ('LED On: Vehicle at intersection...')
            destroy()






#  ----------------------------------------------------------------
#
#  This part of the code set's some additional variables required
#  for the Spark applcation as well as importing the code that
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


