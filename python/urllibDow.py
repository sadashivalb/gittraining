import urllib
import urllib2

import requests

url = 'https://pypi.python.org/packages/source/b/boto/boto-2.9.5.tar.gz#md5=cc79cc87edb4cce00ca275c8ea7b75ed'
print "downloading with urllib"
urllib.urlretrieve(url, "boto.tar.gz")
print "downloading with urllib2"

f = urllib2.urlopen(url)

data = f.read()

with open("boto1.tar.gz", "wb") as code:

   code.write(data)

   print "downloading with requests"
   r = requests.get(url)

with open("boto3.tar.gz", "wb") as code:

   code.write(r.content)
