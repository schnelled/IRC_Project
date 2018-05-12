#!/usr/bin/python
# USAGE:   http_client_urllib2.py <URL>
#           
# EXAMPLE: http_client_urllib2.py http://www.google.com
#
import urllib2,sys

#url = 'http://vsbabu.org/'
url = sys.argv[1]

txdata = None
txheaders = {   
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'gzip, deflate, compress;q=0.9',
    'Keep-Alive': '300',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}
req = urllib2.Request(url, txdata, txheaders)
u = urllib2.urlopen(req)
headers = u.info()
print headers
print u.read()
