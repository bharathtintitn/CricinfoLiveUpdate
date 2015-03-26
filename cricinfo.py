#!/usr/bin/env python
'''
	This script fetches live score from cricinfo
'''
import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
url = "http://static.cricinfo.com/rss/livescores.xml"
match, interrupted = "", False
while True:
    r = requests.get(url)
    try:
	    while r.status_code is not 200:
		    r = requests.get(url)
	    soup = BeautifulSoup(r.text)
	    data = soup.find_all("description")
	    score = data[1].text
	    sendmessage("Score", score)
	    sleep(60)

    except KeyboardInterrupt:

	if interrupted:
		print "bye bye"
		break
	else:
		print "Press ctrl+c again"
		match, interrupted = 0, True

