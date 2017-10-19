#!/usr/bin/env python

import RPi.GPIO as GPIO, time
import sys
import time
import pygame
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin = [11,12,13,15,16,18,22,37]

for io in range(len(pin)):
   GPIO.setup(pin[io], GPIO.OUT)

