#! /usr/bin/env python
#! -*- coding : utf-8 -*-


import psutil
import winsound

def sound():
	frekans = 250
	duration = 100
	winsound.Beep(frekans,duration)

while(1):
	b = psutil.sensors_battery()
	if b[2]:
		continue
	else:
		print("cikartildi")
		sound()


