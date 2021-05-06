from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sha_512 import SHA512
import sys

class Ui_MainWindow(object):
    def __init__(self):
        self.data = b''
        self.readFromFile = False

    def setupUi(self, MainWindow):
        MainWindow.resize(480, 540)
        self.centralwidget = QWidget(MainWindow)

        # create button
        self.browse_button = QPushButton(self.centralwidget)
        self.browse_button.setGeometry(QRect(120, 310, 69, 30))
        self.browse_button.clicked.connect(self.fileBrowser)
        self.gen_button = QPushButton(self.centralwidget)
        self.gen_button.setGeometry(QRect(300, 310, 69, 30))
        self.gen_button.clicked.connect(self.generateHash)
        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QRect(300, 370, 69, 30))
        self.exit_button.clicked.connect(self.exit)
        self.about_button = QPushButton(self.centralwidget)
        self.about_button.setGeometry(QRect(120,370, 69, 30))
        self.about_button.clicked.connect(self.about)

        # create text editor and display hash code
        self.text_edit = QTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QRect(10, 30, 460, 250))
        self.hash_code_display = QPlainTextEdit(self.centralwidget)
        self.hash_code_display.setGeometry(QRect(10, 430, 460, 100))
        self.hash_code_display.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def fileBrowser(self):
        file_browser = QFileDialog(self.centralwidget)
        file_dir = file_browser.getOpenFileName()
        file_dir = file_dir[0]
        with open(file_dir, 'rb') as f:
            self.data = f.read()
            f.close()
        try:
            f = open(file_dir, 'r')
            self.text_edit.setText(f.read())
            f.close()
        except:
            self.text_edit.setText("Can't display file content!")
        file_browser.close()
        self.readFromFile = True
    def generateHash(self):
        if not self.readFromFile:
            self.data = bytearray(self.text_edit.toPlainText(), "utf-8")
        self.hash_code_display.setPlainText(SHA512(self.data).hex_digest().upper())
        self.readFromFile = False
    def exit(self):
        app.exit(0)
    def about(self):
        info = QMessageBox(self.centralwidget)
        info.setText("SHA-512 Hash Generator\t\nAuthor: Dang Dinh Long\t\nEmail: longdang2212@gmail.com\t\nPython & PyQt5\t")
        info.setWindowTitle("About")
        info.show()
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SHA-512 Hash Generator"))
        self.gen_button.setText(_translate("MainWindow", "Generate"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.about_button.setText(_translate("MainWindow", "About"))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())