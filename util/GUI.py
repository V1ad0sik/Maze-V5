from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 230)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 520, 230))
        self.label_2.setStyleSheet("background-color: rgb(20, 20, 30)")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.label.setStyleSheet("background-color: rgb(25, 25, 35);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(500, 0, 20, 21))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: rgb(25, 25, 35);\n"
"  border: none;\n"
"  padding-left: 1px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(28, 28, 32);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: rgb(30, 30, 35);\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(17, 17))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(5, 32, 90, 18))
        self.checkBox.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 75 11pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0097e6;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #00a8ff;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 33, 30, 20))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(255,255,255);\n"
"border: none;\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(138, 57, 31, 16))
        self.label_3.setStyleSheet("font: 75 10pt \"Arial\";\n"
"font-weight: bold;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(5, 55, 121, 20))
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setProperty("value", 7)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(5, 85, 115, 18))
        self.checkBox_2.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 75 11pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0097e6;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #00a8ff;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(5, 105, 121, 20))
        self.horizontalSlider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setProperty("value", 7)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(138, 107, 31, 16))
        self.label_4.setStyleSheet("font: 75 10pt \"Arial\";\n"
"font-weight: bold;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(5, 135, 68, 18))
        self.checkBox_3.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 75 11pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0097e6;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #00a8ff;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 135, 30, 20))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(255,255,255);\n"
"border: none;\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(5, 160, 94, 18))
        self.checkBox_4.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 75 11pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0097e6;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #00a8ff;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(5, 185, 98, 18))
        self.checkBox_5.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 75 11pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0097e6;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #00a8ff;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalSlider_3 = QtWidgets.QSlider(Form)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(5, 205, 121, 20))
        self.horizontalSlider_3.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.horizontalSlider_3.setMinimum(10)
        self.horizontalSlider_3.setMaximum(170)
        self.horizontalSlider_3.setProperty("value", 90)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(138, 207, 31, 16))
        self.label_5.setStyleSheet("font: 75 10pt \"Arial\";\n"
"font-weight: bold;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(180, 30, 2, 191))
        self.label_6.setStyleSheet("background-color: #40739e;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(190, 32, 100, 18))
        self.checkBox_6.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 75 11pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0097e6;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #00a8ff;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.checkBox_6.setObjectName("checkBox_6")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(190, 60, 121, 22))
        self.comboBox.setStyleSheet("QComboBox\n"
"{\n"
"font: 75 10pt \"Arial\";\n"
"border: none;\n"
"background-color: rgb(30,30,30);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border: none;\n"
"    background-color: rgb(100,100,100);\n"
"    font-weight: bold;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalSlider_4 = QtWidgets.QSlider(Form)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(190, 90, 121, 20))
        self.horizontalSlider_4.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.horizontalSlider_4.setMinimum(1)
        self.horizontalSlider_4.setMaximum(20)
        self.horizontalSlider_4.setProperty("value", 3)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(320, 92, 31, 16))
        self.label_7.setStyleSheet("font: 75 10pt \"Arial\";\n"
"font-weight: bold;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(350, 30, 2, 191))
        self.label_8.setStyleSheet("background-color: #40739e;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setGeometry(QtCore.QRect(360, 32, 96, 18))
        self.checkBox_7.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 75 11pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0097e6;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #00a8ff;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Form)
        self.checkBox_8.setGeometry(QtCore.QRect(360, 55, 98, 18))
        self.checkBox_8.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 75 11pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0097e6;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #00a8ff;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Form)
        self.checkBox_9.setGeometry(QtCore.QRect(360, 80, 98, 18))
        self.checkBox_9.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 75 11pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0097e6;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #00a8ff;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.checkBox_9.setObjectName("checkBox_9")
        self.horizontalSlider_5 = QtWidgets.QSlider(Form)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(360, 100, 121, 20))
        self.horizontalSlider_5.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.horizontalSlider_5.setMinimum(0)
        self.horizontalSlider_5.setMaximum(255)
        self.horizontalSlider_5.setProperty("value", 0)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(485, 102, 31, 16))
        self.label_9.setStyleSheet("font: 75 10pt \"Arial\";\n"
"font-weight: bold;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.checkBox_10 = QtWidgets.QCheckBox(Form)
        self.checkBox_10.setGeometry(QtCore.QRect(360, 125, 110, 18))
        self.checkBox_10.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 75 11pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0097e6;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #00a8ff;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.checkBox_10.setObjectName("checkBox_10")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(0, 1, 48, 20))
        self.label_10.setStyleSheet("background-color: rgb(25, 25, 35);\n"
"\n"
"font: 75 12pt \"Arial\";\n"
"color: #3498db;\n"
"padding-left: 1px;")
        self.label_10.setObjectName("label_10")
        self.label_2.raise_()
        self.label.raise_()
        self.checkBox.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.horizontalSlider.raise_()
        self.checkBox_2.raise_()
        self.horizontalSlider_2.raise_()
        self.label_4.raise_()
        self.checkBox_3.raise_()
        self.pushButton_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.horizontalSlider_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.checkBox_6.raise_()
        self.comboBox.raise_()
        self.horizontalSlider_4.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.checkBox_7.raise_()
        self.checkBox_8.raise_()
        self.checkBox_9.raise_()
        self.horizontalSlider_5.raise_()
        self.label_9.raise_()
        self.checkBox_10.raise_()
        self.label_10.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Maze"))
        self.label.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.checkBox.setText(_translate("Form", "Glow ESP"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#f5f6fa;\">0.7</span></p></body></html>"))
        self.checkBox_2.setText(_translate("Form", "Glow ESP HP"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#f5f6fa;\">0.7</span></p></body></html>"))
        self.checkBox_3.setText(_translate("Form", "Chams"))
        self.checkBox_4.setText(_translate("Form", "Global WH"))
        self.checkBox_5.setText(_translate("Form", "Player FOV"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#f5f6fa;\">90</span></p></body></html>"))
        self.checkBox_6.setText(_translate("Form", "Trigget Bot"))
        self.comboBox.setItemText(0, _translate("Form", "M1"))
        self.comboBox.setItemText(1, _translate("Form", "M2"))
        self.comboBox.setItemText(2, _translate("Form", "M3"))
        self.comboBox.setItemText(3, _translate("Form", "M4"))
        self.comboBox.setItemText(4, _translate("Form", "M5"))
        self.comboBox.setItemText(5, _translate("Form", "M6"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#f5f6fa;\">0.3</span></p></body></html>"))
        self.checkBox_7.setText(_translate("Form", "Auto Pistol"))
        self.checkBox_8.setText(_translate("Form", "Bunny Hop"))
        self.checkBox_9.setText(_translate("Form", "No Flash"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#f5f6fa;\">0</span></p></body></html>"))
        self.checkBox_10.setText(_translate("Form", "Show Money"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Maze</span></p></body></html>"))

class Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x_main, y_main = self.geometry().x(), self.geometry().y()
            cursor_x, cursor_y = QtGui.QCursor.pos().x(), QtGui.QCursor.pos().y()

            if x_main <= cursor_x <= x_main + self.geometry().width():
                if y_main <= cursor_y <= y_main + self.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None
        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        try:
                if not self.old_pos:
                    return
                delta = event.pos() - self.old_pos
                self.move(self.pos() + delta)
        except:
                pass