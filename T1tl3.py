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
				url = 'http://'+line2
				try:
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
					result = requests.get(url, headers=headers).content
					soup = bs(result, 'html.parser')
					title = soup.find('title')
					print ('')
					print (' [+] URL Title: ' + str(title.text))
					print (' [+] URL: ' + url)
					print (' [+] URL Status: ' + result.status_code)
				except:
					pass
			except:
				pass
				
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
