import sys
import requests
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import QTextEdit,QWidget,QLineEdit,QRadioButton,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

url="https://www.doviz.com/"
response=requests.get(url)
html_icerigi=response.content
soup=BeautifulSoup(html_icerigi,"html.parser")

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.arayuz()
    def arayuz(self):
        self.degerleri_getir=QPushButton("Döviz değerlerini getir")
        self.metin=QLabel()
        self.degerleri_getir.clicked.connect(self.doviz_degerleri_getir)
        v_box=QVBoxLayout()
        v_box.addWidget(self.degerleri_getir)
        v_box.addWidget(self.metin)
        self.setLayout(v_box)
        self.show()
    def doviz_degerleri_getir(self):
        list_names = list()
        list_values = list()

        for i in soup.find_all("div", {"class": "item"}):

            for x in i.find_all("span", {"class": "name"}):
                x = x.text
                list_names.append(x)

            for y in i.find_all("span", {"class": "value"}):
                y = y.text
                list_values.append(y)

        doviz_sozlugu = dict()
        list2 = zip(list_names, list_values)
        for i, j in list2:
            doviz_sozlugu[i] = j
        metin = ""
        for anahtar, deger in doviz_sozlugu.items():
            metin += f"{anahtar}: {deger}\n"

        self.metin.setText(metin)  # QLabel içeriğini güncelle

app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
