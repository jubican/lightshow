#!/usr/bin/env python

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(11, GPIO.OUT)
# GPIO.setup(5, GPIO.OUT)
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(8, GPIO.OUT)

for num in range(1, 5):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.05)
# time.sleep(2.0)
# time.sleep(2.0)

# GPIO.cleanup()

