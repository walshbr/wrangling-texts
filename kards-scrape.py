#!/usr/bin/env python

import csv
import urllib2
from bs4 import BeautifulSoup

# Base URL for US Magazine. We'll need this to build the full URL for individual
# articles, since it looks like they use relative URLs.
base_url = 'http://www.usmagazine.com'

# Build the full URL to Kim Kardashian's celebrity page.
celebrity_url = base_url + '/celebrities/kim-kardashian?page='

# Hard code range of pages. Quick and dirty.
pages = range(1,138)

newfile = open('usweekly-articles.csv', 'w')
wr = csv.writer(newfile, lineterminator='\n', delimiter=',', escapechar='\\', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
wr.writerow(['title','url'])

# Loop over page ranges, and append the number to the celebrity_url
for p in enumerate(pages):
    page_string = str(p)
    soup = BeautifulSoup(urllib2.urlopen(celebrity_url + page_string).read())

    # Find all the articles on each page.
    for article in soup.find_all('article', {'class': 'celebrity-news-article'}):
        title = article.h3.contents[0].encode('utf-8')
        url = article.a['href'].encode('utf-8')
        url = base_url + url
        row = [title, url]
        wr.writerow(row)
