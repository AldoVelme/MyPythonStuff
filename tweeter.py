#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AdminPortal1.1.py
#
#  Copyright 2017 AVELAZCX <aldo.alfonsox.velasco.meza@intel.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import tweepy, os

def getStatus():
    lines = []
    while True:
        line = raw_input()
        if line:
            lines.append(line)
        else:
            break
    status = '\n'.join(lines)
    return status

def tweetthis(type):
	if type == "text":
		print "Enter your tweet "+user.name
		tweet = getStatus()
		try:
			api.update_status(tweet)
		except Exception as e:
			print e
			return
	elif type == "pic":
		print "Enter pic path "+user.name
		pic = os.path.abspath(raw_input())
		print "Enter status "+user.name
		title = getStatus()
		try:
			api.update_with_media(pic, status=title)
		except Exception as e:
			print e
			return

	print "\n\nDONE!!"

def initialize():
	global api, auth, user
	ck = "here" # consumer key
	cks = "here" # consumer key SECRET
	at = "here" # access token
	ats = "here" # access token SECRET

	auth = tweepy.OAuthHandler(ck,cks)
	auth.set_access_token(at,ats)

	api = tweepy.API(auth)
	user = api.me()

def main():
	doit = int(raw_input("\n1. text\n2. picture\n"))
	initialize()
	if doit == 1:
		tweetthis("text")
	elif doit == 2:
		tweetthis("pic")
	else:
		print "OK, Let's try again!"
		main()

main()
