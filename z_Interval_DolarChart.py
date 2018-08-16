#! /usr/bin/env python
#! -*- coding = utf-8 -*-


import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import urllib
import requests
import time
import sys




def DParse():

    pasteURL = "https://kur.doviz.com/serbest-piyasa/amerikan-dolari"
    time.sleep(int(sys.argv[1]))
    data = urllib.urlopen(pasteURL).read()
    parse = BeautifulSoup(data)
    kur = parse.find_all('span', attrs={'class':'color-red'})[1]
    pstr = str(kur)[24:][:6]
    print "%s" %str(kur)[24:][:6]
    return pstr


plt.plot([int(sys.argv[1]),int(sys.argv[1])*2,int(sys.argv[1])*3],[DParse(),DParse(),DParse()])
plt.title('Time Interval Dollar Chart')
plt.ylabel("Dolar")
plt.xlabel("Second")


plt.show()

