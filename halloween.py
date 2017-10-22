#/usr/bin/env python

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

with open(sys.argv[1], 'r') as f:
  data = f.readlines()
  for i in range(len(data)):
    data[i] = data[i].rstrip()

inittime = int(round(time.time()*1000))
step = 1

main_section = "primary_section"
currlist = main_section
seqlist = []
proclist = []

# pygame.mixer.init()
# pygame.mixer.music.load(sys.argv[2])
# pygame.mixer.music.play()

while True:
  line = data[step].strip().lower()
  
  if line.startswith("#") or not line:
    step += 1
    continue
  elif line.startswith("routine_start"):
    r_temp = line.split()
    seqlist[r_temp[1]] = []
    currlist = t_temp[1]
  elif line.startswith("routine_end"):
    currlist = main_section
  elif "," in line:
    current = line.split(",")
    if current[0] == "routine" and seqlist[current[1]]:
      num = int(current[2])
      for itm in seqlist[current[1]]:
        seqlist[main_section].append([num+itm[0], itm[1], itm[2]])
    else:
      num = int(current[0])
      lit = int(current[1])
      cmd = int(current[2])
      seqlist[currlist].append([num, lit, cmd])
    
    #curtime = int(round(time.time()*1000)) - inittime
    #stime = int(current[0]) + 550
    #spin = int(current[1].lstrip())
    #svalue = int(current[2])
    
    #if stime <= curtime:
    #  if spin >= 1 and spin <= 8:
    #    print current
      
        # if svalue == 1:
        #   GPIO.output(pin[spin-1], GPIO.HIGH)
        # else:
        #   GPIO.output(pin[spin-1], GPIO.LOW)
  elif line == "end":
    #for i in range(len(pin)):
    #  GPIO.output(pin[i], GPIO.LOW)
    break
    
  step += 1

# pygame.mixer.music.stop()
