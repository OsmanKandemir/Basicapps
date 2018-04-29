#! /usr/bin/env python
#! -*- coding : utf-8 -*-


import re
import tweepy
import sys



def login(key,secret,access,access_sec):
	consumer_key = key
	consumer_secret = secret
	access_key = access
	access_secret = access_sec
	g = tweepy.OAuthHandler(consumer_key, consumer_secret)
	g.set_access_token(access_key, access_secret)
	api = tweepy.API(g)
	return api
	

def postlar(ap):
	i = 0
	hepsi = ap.user_timeline(count=200)
	
	for h in hepsi:
		print str(i) +" >>> " +  h.text.encode('utf-8') 
		print("-------------------------------------------------------")
		i = i + 1
	while(1):

		dele = input("Delete tweet id")
		sil = compare(ap,dele)
		ap.destroy_status(sil)
		postlar(ap)


def compare(ap2,deger):
	b = 0
	hepsi = ap2.user_timeline(count=200)
	for h in hepsi:
		if(deger == b):
			iddegeri = h.id
			return iddegeri
		else:
			b = b + 1
		



giris = login(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

postlar(giris)
