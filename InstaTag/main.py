
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("UI파일이름.ui")[0]

baseUrl = 'https://www.instagram.com/'
plusUrl = input('Instagram User ID : ')
url = baseUrl + quote_plus(plusUrl)

url = baseUrl + quote_plus(plusUrl)

print(url)

driver = webdriver.Chrome()
driver.get(url)


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


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btnSearch.clicked.connect(self.buttonSearch)

    def buttonSearch(self) :
        print("btn1 cliked")
        plusUrl = lineEdit


    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    # def insta(self):


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
