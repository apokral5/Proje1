import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.kaydet=QPushButton("Kaydet")
        self.temizle=QPushButton("Temizle")
        v_box=QVBoxLayout()
        v_box.addWidget(self.yazi_alani)

        h_box=QHBoxLayout()
        h_box.addWidget(self.kaydet)
        h_box.addWidget(self.temizle)

        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("Kullanıcı girişi")
        self.kaydet.clicked.connect(self.metni_kaydetme)
        self.temizle.clicked.connect(self.metni_temizle)
        self.show()
    def metni_kaydetme(self):
        dosya_ismi=QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("Home"))
        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())
    def metni_temizle(self):
        self.yazi_alani.clear()

app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
