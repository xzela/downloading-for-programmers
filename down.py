from lxml import html
import urllib2

def get_page(url):
	page = urllib2.urlopen(url)
	tree = html.fromstring(page.read())
	music_xpath = '/html/body/div[2]/div/a[1]'
	file_a = tree.xpath(music_xpath)
	return [file_a[0].text, file_a[0].attrib['href']]

url = 'http://musicforprogramming.net/' 
page = urllib2.urlopen(url)
tree = html.fromstring(page.read())
links = tree.xpath('/html/body/div[3]/div[1]/div/a');
for a in links:
	nurl = url + a.attrib['href']
	data = get_page(nurl)
	print "downloading: %s to %s" % (data[1], data[0])
	res = urllib2.urlopen(data[1])
	fh = open(data[0], "w")
	fh.write(res.read())
	fh.close();
	#urllib2.urlretrieve(data[1], data[0])


