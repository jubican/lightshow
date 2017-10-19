#/usr/bin/env python

import RPi.GPIO as GPIO, time
import sys
import time
import pygame
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# pin = [11,12,13,15,16,18,22,37]
pin = [11,12,13]

for io in range(len(pin)):
   GPIO.setup(pin[io], GPIO.OUT)

with open(sys.argv[1], 'r') as f:
  data = f.readlines()
  for i in range(len(data)):
    data[i] = data[i].rstrip()

inittime = int(round(time.time()*1000))
step = 1

pygame.mixer.init()
pygame.mixer.music.load(sys.argv[2])
pygame.mixer.music.play()

while True:
  current = data[step].split(",")
  curtime = int(round(time.time()*1000)) - inittime
  stime = int(current[0]) + 550
  spin = int(current[1].lstrip())
  svalue = int(current[2])
  
  print current
  
  if stime <= curtime:
    if spin >= 1 and spin <= 8:
      if svalue == 1:
        GPIO.output(pin[spin-1], GPIO.HIGH)
      else:
        GPIO.output(pin[spin-1], GPIO.LOW)
    
    if spin <= 0:
      for i in range(len(pin)):
        GPIO.output(pin[i], GPIO.LOW)
      break
    
    step += 1

pygame.mixer.music.stop()

# GPIO.output(pin[0], GPIO.HIGH)
# time.sleep(0.100)
# GPIO.output(pin[0], GPIO.LOW)
# time.sleep(0.240)
#
# GPIO.output(pin[0], GPIO.HIGH)
# time.sleep(0.100)
# GPIO.output(pin[0], GPIO.LOW)
# time.sleep(0.240)
#
# GPIO.output(pin[1], GPIO.HIGH)
# time.sleep(0.340)
# GPIO.output(pin[1], GPIO.LOW)
# GPIO.output(pin[2], GPIO.HIGH)
# time.sleep(0.340)
# GPIO.output(pin[2], GPIO.LOW)


