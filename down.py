from lxml import html
import urllib
import requests

def get_page(url):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	music_xpath = '/html/body/div[2]/div/a[1]'
	file_a = tree.xpath(music_xpath)
	return [file_a[0].text, file_a[0].attrib['href']]

url = 'http://musicforprogramming.net/' 
page = requests.get(url)
tree = html.fromstring(page.content)
links = tree.xpath('/html/body/div[3]/div[1]/div/a');
for a in links:
	nurl = url + a.attrib['href']
	data = get_page(nurl)
	print "downloading: %s to %s" % (data[1], data[0])
	urllib.urlretrieve(data[1], data[0])

