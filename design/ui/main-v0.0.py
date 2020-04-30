from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import webbrowser
from lib.ipfs import ipfs
#from PyQt5 import QtCore, QtGui, QtWidgets,


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 550)
        MainWindow.setMinimumSize(QtCore.QSize(820, 550))
        MainWindow.setMaximumSize(QtCore.QSize(820, 550))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 820, 550))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("design/png/background.png"))
        self.label.setObjectName("label")
        self.browse_file_btn = QtWidgets.QLabel(self.centralwidget)
        self.browse_file_btn.setGeometry(QtCore.QRect(430, 160, 221, 51))
        self.browse_file_btn.setText("")
        self.browse_file_btn.setObjectName("browse_file_btn")
        self.web_panel_btn = QtWidgets.QLabel(self.centralwidget)
        self.web_panel_btn.setGeometry(QtCore.QRect(40, 90, 181, 51))
        self.web_panel_btn.setText("")
        self.web_panel_btn.setObjectName("web_panel_btn")
        self.github_btn = QtWidgets.QLabel(self.centralwidget)
        self.github_btn.setGeometry(QtCore.QRect(0, 180, 261, 41))
        self.github_btn.setText("")
        self.github_btn.setObjectName("github_btn")
        self.ipfs_btn = QtWidgets.QLabel(self.centralwidget)
        self.ipfs_btn.setGeometry(QtCore.QRect(0, 230, 261, 41))
        self.ipfs_btn.setText("")
        self.ipfs_btn.setObjectName("ipfs_btn")
        self.file_btn = QtWidgets.QLabel(self.centralwidget)
        self.file_btn.setGeometry(QtCore.QRect(510, 60, 61, 71))
        self.file_btn.setText("")
        self.file_btn.setObjectName("file_btn")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(320, 358, 441, 16))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(11)
        self.result_label.setFont(font)
        self.result_label.setAutoFillBackground(False)
        self.result_label.setStyleSheet("color : white;")
        self.result_label.setObjectName("result_label")
        self.file_label = QtWidgets.QLabel(self.centralwidget)
        self.file_label.setGeometry(QtCore.QRect(320, 260, 431, 61))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕 UltraLight")
        font.setPointSize(10)
        self.file_label.setFont(font)
        self.file_label.setObjectName("file_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.github_btn.mouseReleaseEvent = self.github_label_clicked
        self.ipfs_btn.mouseReleaseEvent = self. ipfs_label_clicked
        self.browse_file_btn.mouseReleaseEvent = self.file_upload_clicked
        self.file_btn.mouseReleaseEvent = self.file_upload_clicked

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IPFS-GUI"))
        self.result_label.setText(_translate("MainWindow", "TextLabel"))
        self.file_label.setText(_translate("MainWindow", "TextLabel"))

    def github_label_clicked(self, event):
        url = 'https://github.com/ytype'
        webbrowser.open(url)

    def ipfs_label_clicked(self, event):
        url = 'https://ipfs.io/'
        webbrowser.open(url)

    def file_upload_clicked(self,event):
        fileName = QFileDialog.getOpenFileName(None, 'Dialog Title', '')
        self.file_label.setText(fileName[0])
        self.result_label.setText("file selected")


if __name__ == "__main__":
    ipfs = ipfs()
    ipfs.isWindows64()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
