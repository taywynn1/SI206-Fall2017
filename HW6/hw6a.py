from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

l = list()
for tag in soup.find_all('span'):
	numbers = int(tag.string)
	#print(numbers)
	l.append(numbers)
total = sum(l)
print(total)