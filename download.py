import os
import urllib2
import base64
f = open("poms.txt")

poms = []

for line in f.readlines():
	poms.append(line)

f.close()

print "alle poms gelesen: ", len(poms)
		
count = 1
for url in poms:
	print count, " / ", len(poms)
	if not os.path.exists(os.path.join("poms/",  base64.encodestring(url))):
		pom = urllib2.urlopen(url).read()
		f = open(os.path.join("poms/", base64.encodestring(url)), "w")
		f.write(pom)
		f.close()
	count +=1
	