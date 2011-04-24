import urllib2
import time
import codecs
from BeautifulSoup import BeautifulSoup




def getChildren(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	list = soup.findAll("a")

	dirs = []
	poms = []
	for link in list:
		href = link.contents[0]
		if href != None:
			href = href.encode("utf-8")
			if href != "../" and href.endswith("/"):
				dirs.append(url + href)
			if href.endswith(".pom"):
				poms.append(url + href)
	return dirs, poms
		


def writePomUrl(list):
	f = file("poms.txt", "a")
	for pomurl in list:
		f.write(pomurl + "\r\n")
	f.close()


def getPoms(url):
	dirs, poms = getChildren(url)
	writePomUrl(poms)
	print dirs
	
	
	
	while len(dirs) > 0:
		for dir in dirs:
			print dir
			try:
				rdirs, rpoms = getChildren(dir)
			#print rdirs
			#print rpoms
				writePomUrl(rpoms)
				dirs = dirs + rdirs
			except:
				print "error", dir
			#print dir
			dirs.remove(dir)
			 
		
	
	

baseurl = "http://repo1.maven.org/maven2/"
	

getPoms(baseurl)




	


#print dirs, poms