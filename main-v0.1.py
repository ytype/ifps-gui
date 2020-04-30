from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import webbrowser
from lib.ipfs import ipfs

class Ui_MainWindow(object):
    def __init__(self):
        self.ipfs = ipfs()

    def setupUi(self, MainWindow):
        self.file_name = ''
        self.hash = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 550)
        MainWindow.setMinimumSize(QtCore.QSize(820, 550))
        MainWindow.setMaximumSize(QtCore.QSize(820, 550))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_image = QtWidgets.QLabel(self.centralwidget)
        self.background_image.setGeometry(QtCore.QRect(0, 0, 820, 550))
        self.background_image.setText("")
        self.background_image.setPixmap(QtGui.QPixmap("design/png/background.png"))
        self.background_image.setObjectName("background_image")
        self.file_icon = QtWidgets.QLabel(self.centralwidget)
        self.file_icon.setGeometry(QtCore.QRect(480, 37, 119, 119))
        self.file_icon.setText("")
        self.file_icon.setPixmap(QtGui.QPixmap("design/png/iconfinder_document-upload_4918890.png"))
        self.file_icon.setObjectName("file_icon")
        self.browse_upload_btn = QtWidgets.QLabel(self.centralwidget)
        self.browse_upload_btn.setGeometry(QtCore.QRect(428, 156, 222, 59))
        self.browse_upload_btn.setText("")
        self.browse_upload_btn.setPixmap(QtGui.QPixmap("design/png/browse.png"))
        self.browse_upload_btn.setObjectName("browse_upload_btn")
        self.pannel_btn = QtWidgets.QLabel(self.centralwidget)
        self.pannel_btn.setGeometry(QtCore.QRect(37, 94, 189, 47))
        self.pannel_btn.setText("")
        self.pannel_btn.setPixmap(QtGui.QPixmap("design/png/init.png"))
        self.pannel_state = 'init'
        self.pannel_btn.setObjectName("pannel_btn")

        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(320, 358, 441, 16))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(11)
        self.result_label.setFont(font)
        self.result_label.setAutoFillBackground(False)
        self.result_label.setStyleSheet("color : white;")
        self.result_label.setObjectName("result_label")

        self.download_btn = QtWidgets.QLabel(self.centralwidget)
        self.download_btn.setGeometry(QtCore.QRect(728, 296, 32, 32))
        self.download_btn.setText("")
        self.download_btn.setObjectName("download_btn")

        self.file_title_label = QtWidgets.QLabel(self.centralwidget)
        self.file_title_label.setGeometry(QtCore.QRect(410, 220, 431, 61))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(12)
        self.file_title_label.setFont(font)
        self.file_title_label.setObjectName("file_label")

        self.file_label = QtWidgets.QLabel(self.centralwidget)
        self.file_label.setGeometry(QtCore.QRect(410, 240, 431, 61))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(10)
        self.file_label.setFont(font)
        self.file_label.setObjectName("file_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.detectWin64()

        self.file_icon.mouseReleaseEvent = self.file_select_upload
        self.browse_upload_btn.mouseReleaseEvent = self.file_select_upload
        self.pannel_btn.mouseReleaseEvent = self.pannel_click
        self.download_btn.mouseReleaseEvent = self.download_file

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def download_file(self, event):
        if(self.hash != ''):
            url = 'https://gateway.ipfs.io/ipfs/'
            webbrowser.open(url+self.hash)
        else:
            self.result_label.setText('no file')


    def detectWin64(self):
        if(self.ipfs.isWindows64()):
            self.result_label.setText('win64 detected')
        else:
            self.result_label.setText('ipfs version is win/64 plz download your version')

    def pannel_click(self, event):
        if(self.pannel_state=='init'):
            if(self.ipfs.init()==True):
                self.pannel_btn.setPixmap(QtGui.QPixmap("design/png/start.png"))
                self.pannel_state = 'start'
                self.result_label.setText('ipfs init')
            else:
                self.result_label.setText('ipfs init error')

        elif(self.pannel_state=='start'):
            if(self.ipfs.daemon()==True):
                self.pannel_btn.setPixmap(QtGui.QPixmap("design/png/web.png"))
                self.pannel_state = 'web'
                self.result_label.setText('ipfs daemon start')
            else:
                self.result_label.setText('ipfs daemon error')

        elif(self.pannel_state=='web'):
            url = 'http://localhost:5001/webui'
            webbrowser.open(url)

    def file_select_upload(self, event):
        if(self.file_name==''):
            fileName = QFileDialog.getOpenFileName(None, 'select file', '')
            self.file_name = fileName[0]
            self.result_label.setText(f'file selected: {self.file_name}')
            self.file_icon.setPixmap(QtGui.QPixmap("design/png/file_selected.png"))
            self.browse_upload_btn.setPixmap(QtGui.QPixmap("design/png/upload.png"))
        else:
            result = self.ipfs.add(self.file_name)
            if(result):
                self.hash = result
                self.file_label.setText(result)
                self.file_title_label.setText(self.file_name.split('/')[-1])
                self.result_label.setText('file uploaded')
            else:
                self.result_label.setText('ipfs add error')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
