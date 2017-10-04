from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')
print('Retrieving: ', url)
for number in range(int(count)):
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	tag = soup.find_all('a')[int(position) -1]
	url = tag.attrs['href']
	print("Retrieving: ", url)

	
