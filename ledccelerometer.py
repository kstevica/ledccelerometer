#!/usr/bin/env python
# coding: latin-1
# script by Stevica Kuharski, @kstevica

import XLoBorg
import time
import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.output(11, False)
GPIO.output(13, False)
GPIO.output(15, False)

XLoBorg.printFunction = XLoBorg.NoPrint

XLoBorg.Init()

old_x, old_y, old_z = XLoBorg.ReadAccelerometer()

use_sensitivity = 1

def light(pin, on_off):
	GPIO.output( pin, on_off)

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
	old_x = x
	old_y = y
	old_z = z
	light(11, should_x)
	light(13, should_y)
	light(15, should_z)
	if (should_x or should_y or should_z):
		time.sleep(1)

	time.sleep(0.1)
