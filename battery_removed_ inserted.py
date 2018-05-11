#! /usr/bin/env python
#! -*- coding : utf-8 -*-


import psutil
import winsound
import time


def sound():
	frekans = 1000
	duration = 1000
	winsound.Beep(frekans,duration)
h = False
h2 = False
while(1):
	b = psutil.sensors_battery()

	if b[2]:
                if not h:
                        print("Sarj Takili Durumda")
                        h = True
                h2 = False
	else:
                if not h2:
                        print("Sarjdan Cikarildi")
                        h2 = True
                sound()       
		h = False
                
		

