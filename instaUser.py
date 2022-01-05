from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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


action = ActionChains(driver)

driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF').click()
action.send_keys('cafe._.life').perform()


time.sleep(3)

SCROLL_PAUSE_SEC = 5

# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

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
