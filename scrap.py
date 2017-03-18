import urllib2
from bs4 import BeautifulSoup
link="http://blog.aiesec.in/"
page=urllib2.urlopen(link).read()
soup=BeautifulSoup(page,"html.parser")
a = soup.find_all("div",{"class":"post-item"})
for i in a:
    title=i.findAll("h2")
    for x in title:
        can = x.findAll("a")
        print can[0].contents

