import urllib2
import time
import codecs
from BeautifulSoup import BeautifulSoup




def parsePoms(url):
	page = open(url, "r").read()
	soup = BeautifulSoup(page)
	
	try:
		version = soup.project.version.contents[0].encode("utf-8")
		if version.endswith("-SNAPSHOT"):
			return
	except:
		print "ERROR!"
	
		
	list = soup.findAll("version")
	for version in list:
		try:
			version = version.contents[0].encode("utf-8")
			if version.endswith("-SNAPSHOT"):
				print "OJEE OJEEEEEE", soup.project.groupid, soup.project.artifactid, soup.project.version 
			else:
				pass
				#print url
		except:
			print "ERROR"

import os

poms = os.listdir("poms/")



print "alle poms gelesen"
		
for url in poms:
	parsePoms(os.path.join("poms", url))
		