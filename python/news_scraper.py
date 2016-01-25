import urllib
from BeautifulSoup import BeautifulSoup 

url = "http://www.nst.com.my/news/2015/09/haze-19-areas-records-unhealthy-air-quality"

page = urllib.urlopen(url)
html = page.read()

#print html
soup = BeautifulSoup(html)

mydivs = soup.findAll("div", { "class" : "node-content content" })

content = mydivs[0].text

print content