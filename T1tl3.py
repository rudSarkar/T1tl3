#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Rudra Sarkar
# Twitter: @rudr4_sarkar
# T1tl3.py

import sys
import requests
from bs4 import BeautifulSoup as bs


def usage():
	print ('')
	print ('$ python ' + sys.argv[0] + ' urlList.txt')

def banner():
	print ('''
	  _______   __   _     _   ____  
	 |__   __| /_ | | |   | | |___ \ 
	    | |     | | | |_  | |   __) |
	    | |     | | | __| | |  |__ < 
	    | |     | | | |_  | |  ___) |
	    |_|     |_|  \__| |_| |____/ 

	    By Rudra Sarkar, Twitter: @rudr4_sarkar                          
	''')

def checkTitle(argv):
	file = argv
	with open(file) as f:
		for line in f:
			try:
				line2 = line.strip()
				url = 'https://'+line2
				try:
					result = requests.get(url)
					soup = bs(result.content, 'html.parser').encode("utf-8")
					title = soup.select_one('title').text
					print ('')
					print (' [+] URL Title: ' + title)
					print (' [+] URL: ' + url)
					print (' [+] URL Status: ' + result.status_code)
				except:
					print ('')
					print (' [x] No title found')
					print (' [x] URL: ' + url)
					print (' [x] URL Status: ' + result.status_code)
			except:
				print (' [x] Error')
				
if (len(sys.argv)) == 2:
	try:
		print ('')
		banner()
		print ('')
		print (' [+] Scanning start ...')
		checkTitle(sys.argv[1])
	except:
		print ('')
		print (' [x] Can\'t find your ' + sys.argv[1] + ' file.')
else:
	usage()
	sys.exit(0)
