'''

This routine is used to test the operation of the Raspberry Pi sensor.

This project was conceived as a means to introduce coding, IoT sensors and cloud applications to high school students.
The project focuses on autonomous vehicles using the Raspberry Pi to simulate a sensor and the and the Cisco Spark 
service to simulate a cloud based application server.

The use case was conceived from research done by University of Texas, Austin published in this video:
https://www.youtube.com/watch?v=4pbAI40dK0A

This project's objective is to simulate the implementation of an Autonomous Intersection Management Traffic 
Control System.

The Raspberry Pi was build with a sensor kit from Sunfounder:
https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-2-controlling-an-led-by-a-button-super-kit-for-raspberrypi.html

The source code for the Sunfounder Raspberry was modified and integrated with the Cisco Spark API's and application 
logic. The original source code can be found at:
https://github.com/sunfounder/Sunfounder_SuperKit_Python_code_for_RaspberryPi/blob/master/02_btnAndLed.py

This project was implemented with Python 2.7 running on the Raspberry Pi.

'''


#!/usr/bin/env python

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

print (Led_status)


#  ----------------------------------------------------------------
#
#  NOTE: Do not modify any of this code above this line !!!
#
#  ----------------------------------------------------------------


# --- Modify variables below based on your group -----


token = ''

roomId = ''

img_go = ''

img_stop = ''

reservationToken = ''


# --- Modify variables above based on your group -----







