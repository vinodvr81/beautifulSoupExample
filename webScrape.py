import urllib.request
import ssl
from bs4 import BeautifulSoup
import datetime
import sqlite3



class webscrapeurl():

    def __init__(self):
        pass
    def dataWebscrape(self):

        context = ssl._create_unverified_context()
        parentURL= 'https://github.com/vinodvr81'
        webpage = urllib.request.urlopen(parentURL,context=context).read()

        soup = BeautifulSoup(webpage, "html5lib")
        doc = soup.prettify()
        fh = open("githubVinodvr81.html", "w")  
        fh.write(doc)  
        fh.close()

f = webscrapeurl()
f.dataWebscrape()
