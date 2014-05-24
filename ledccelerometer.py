#!/usr/bin/env python
# coding: latin-1
# coded by Stevica Kuharski, @kstevica

import XLoBorg
import time
import RPi.GPIO as GPIO
import math

# pins that you'll use
use_pin_x = 11
use_pin_y = 13
use_pin_z = 15

# setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(use_pin_x, GPIO.OUT)
GPIO.setup(use_pin_y, GPIO.OUT)
GPIO.setup(use_pin_z, GPIO.OUT)
GPIO.output(use_pin_x, False)
GPIO.output(use_pin_y, False)
GPIO.output(use_pin_z, False)

# XLoBorg initialization
XLoBorg.printFunction = XLoBorg.NoPrint
XLoBorg.Init()

# init globals
old_x, old_y, old_z = XLoBorg.ReadAccelerometer()
use_sensitivity = 1

# setup software PWM
light_x = GPIO.PWM(use_pin_x, 100)
light_y = GPIO.PWM(use_pin_y, 100)
light_z = GPIO.PWM(use_pin_z, 100)

# turn light on
def light(pin, on_off, strength):
	if (on_off==True):
		strength = min(strength*200, 100)
		pin.start(strength)
	else:
		pin.stop()

# main loop
while True:
	should_x = False
	should_y = False
	should_z = False
	x,y,z = XLoBorg.ReadAccelerometer()
	x = round(x, use_sensitivity)
	y = round(y, use_sensitivity)
	z = round(z, use_sensitivity)
        if (z!=old_z):
		should_z = True
	if (x!=old_x):
		should_x = True
	if (y!=old_y):
		should_y = True
	light(light_x, should_x, abs(old_x-x))
	light(light_y, should_y, abs(old_y-y))
	light(light_z, should_z, abs(old_z-z))
	if (should_x or should_y or should_z):
		time.sleep(0.5)
        old_x = x
        old_y = y
        old_z = z
