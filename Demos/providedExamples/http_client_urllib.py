#!/usr/bin/python
# USAGE:   http_client_urllib.py <URL>
#           
# EXAMPLE: http_client_urllib.py http://www.google.com
#
import urllib, sys
from sgmllib import SGMLParser
class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):
        href = [v for k, v in attrs if k=='href']
        if href:
            self.urls.extend(href)

sock = urllib.urlopen(sys.argv[1])
htmlSource = sock.read()
sock.close()
print htmlSource

parser = URLLister()
parser.feed(htmlSource)
parser.close()
for url in parser.urls: print url
