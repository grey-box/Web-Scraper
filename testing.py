#!/usr/bin/env python
import urllib.request as urllib2
from bs4 import *
from urllib.parse import urljoin
import os

# This is just a simple python file only to test certain code to see if it works.
# Not used for anything else

def crawl(pages, depth=None):
    indexed_url = [] # a list for the main and sub-HTML websites in the main website
    for i in range(depth):
        for page in pages:
            if page not in indexed_url:
                indexed_url.append(page)
                try:
                    c = urllib2.urlopen(page)
                except:
                    print( "Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read())
                links = soup('a') #finding all the sub_links
                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                            continue
                        url = url.split('#')[0]
                        if url[0:4] == 'http':
                            indexed_url.append(url)
        pages = indexed_url
    return indexed_url


pagelist=["https://en.wikipedia.org/wiki/Python_%28programming_language%29"]
urls = crawl(pagelist, depth=1)
# print( urls )


from pywebcopy import save_website

url = 'http://www.reirab.com/comp551.html'
download_folder = os.getcwd()

kwargs = {'bypass_robots': True, 'project_name': 'PyWebCopy'}

save_website(url, download_folder, **kwargs)