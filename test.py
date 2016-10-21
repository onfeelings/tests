# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:36:46 2016

@author: luhui
"""

from urllib import urlopen 
from bs4 import BeautifulSoup 
url ='http://www.pythonscraping.com/pages/page1.html'
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "lxml")

print bsObj.h1
