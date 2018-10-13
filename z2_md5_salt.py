#! /usr/bin/env python
#! -*- coding : utf-8 -*-

import hashlib
import sys

print """
     
    Name : Md5 + Salt Simple Decoder And Compare
    	  
      """   
#how to use -> python z2_md5_salt.py md5 salt

def md5(text):
	return hashlib.md5(text).hexdigest()

try:
	has = sys.argv[1]
	salt = sys.argv[2]
	pw = ["123456","deneme"]
except:
	sys.exit()

for i in pw:
	ha = md5(md5(i)+salt)
	if has==ha:
		print "Found : " + i + " \t" + "Hash : " + ha

	else:
		print "Not Found"
