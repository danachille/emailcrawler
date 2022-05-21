import requests
import re
import time
from bs4 import BeautifulSoup

print("  _____    _____         __       ")
print(" / ___/___/ ___ \_    __/ /__ ____")
print("/ /__/ __/ / _ `/ |/|/ / / -_) __/")
print("\___/_/  \ \_,_/|__,__/_/\__/_/   ")
print("  v1.0 by \___/  Dan Achille   ")
print(" ")



url = input('Enter url to crawl (FQDN without ending /) : ')
level = input('Level of crawling (Can be really slow) : ')
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

raw_urls = []
for link in soup.find_all('a'):
    raw_urls.append(link.get('href'))

r=re.compile("^/")
filtered_urls = list(filter(r.match, raw_urls))
filtered_urls = list(dict.fromkeys(filtered_urls))
print("Urls Found: ", len(filtered_urls))

for u in range(0,int(level)-1):
    raw_urls = []
    for i in filtered_urls:
        print("Processing ",url+i)
        reqs = requests.get(url+i)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        for link in soup.find_all('a'):
            if link.get('href') is not None :
                raw_urls.append(link.get('href'))
        time.sleep(0.1)

    filtered_urls = list(filter(r.match, raw_urls))
    filtered_urls = list(dict.fromkeys(filtered_urls))
    print("Link Found with Crawling Level "+level)
    print(len(filtered_urls))

mailto = []
email_list = []

for i in filtered_urls:
    reqs = requests.get(url+i)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    print("Processing ",url+i)
    mailto = soup.select('a[href^=mailto]')
    for i in mailto:
        href = i['href']
        try:
            str1, str2 = href.split(':')
        except ValueError:
            break

        email_list.append(str2)

email_list = list(dict.fromkeys(email_list))
print('\n'.join(email_list))
print("Number of crawled emails : ",len(email_list))