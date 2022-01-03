from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

import time

print('=========================================================')
print('Instagram  Image  Download')
print('ver.2.0.3')
print('Chrome:90.0.4430.212')
print('V8 9.0.257.29')
print('=========================================================')
print('')
print('')

baseUrl = 'https://www.instagram.com/'
plusUrl = input('Instagram User ID : ')
url = baseUrl + quote_plus(plusUrl)

print(url)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select('.v1Nh3.kIKUG._bz0w')

n = 1
for i in insta:
    print('https://www.instagram.com/' + i.a['href'])
    imgUrl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgUrl) as f:
        with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
    print()

driver.close()
