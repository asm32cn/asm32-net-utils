# py-dl-image.py

import urllib2, re, os

# urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({'http':'10.1.1.6:8081'})))
urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({'http':'10.1.1.6:33080'})))

# url = 'http://www.asm32.net/article-details-7317.aspx'
# url = 'http://www.asm32.net/article-details-7318.aspx'
url = 'http://www.asm32.net/article-details-7291.aspx'


conf__strFind = (
	'<!-- Article strContent : Start -->',
	'<!-- Article strContent : End -->'
)

data = urllib2.urlopen(url).read()
nFind = data.find(conf__strFind[0])
if nFind >= 0:
	nFind += len(conf__strFind[0])
	data = data[nFind : data.find(conf__strFind[1],nFind)]

	urlPrefix = url[:url.rfind('/') + 1]

	images = re.findall('<img.*?src="(.*?)".*?[/]?>', data)
	for strFile in images:
		nPos = strFile.rfind('/')
		if nPos:
			strFolder = strFile[:nPos]
			if not os.path.exists(strFolder):os.makedirs(strFolder)
			# print 'folder:', strFolder

		print strFile
		with open(strFile, 'wb') as fo:
			fo.write(urllib2.urlopen(urlPrefix + strFile).read())

	# print images
	# print urlPrefix

print nFind

# url = 'http://www.asm32.net/pic/article/i7318_001.png'


