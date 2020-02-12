# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'console.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsoleWindow(object):
    def setupUi(self, ConsoleWindow):
        ConsoleWindow.setObjectName("ConsoleWindow")
        ConsoleWindow.setWindowModality(QtCore.Qt.NonModal)
        ConsoleWindow.resize(800, 612)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConsoleWindow.sizePolicy().hasHeightForWidth())
        ConsoleWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ConsoleWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.downbutton = QtWidgets.QPushButton(self.centralwidget)
        self.downbutton.setObjectName("downbutton")
        self.horizontalLayout_2.addWidget(self.downbutton)
        self.lineEndComboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEndComboBox.sizePolicy().hasHeightForWidth())
        self.lineEndComboBox.setSizePolicy(sizePolicy)
        self.lineEndComboBox.setObjectName("lineEndComboBox")
        self.lineEndComboBox.addItem("")
        self.lineEndComboBox.addItem("")
        self.lineEndComboBox.addItem("")
        self.lineEndComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.lineEndComboBox)
        self.baudRateComboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baudRateComboBox.sizePolicy().hasHeightForWidth())
        self.baudRateComboBox.setSizePolicy(sizePolicy)
        self.baudRateComboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.baudRateComboBox.setObjectName("baudRateComboBox")
        self.horizontalLayout_2.addWidget(self.baudRateComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        ConsoleWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConsoleWindow)
        QtCore.QMetaObject.connectSlotsByName(ConsoleWindow)

    def retranslateUi(self, ConsoleWindow):
        _translate = QtCore.QCoreApplication.translate
        ConsoleWindow.setWindowTitle(_translate("ConsoleWindow", "MainWindow"))
        self.sendButton.setText(_translate("ConsoleWindow", "Send"))
        self.downbutton.setText(_translate("ConsoleWindow", "To end"))
        self.lineEndComboBox.setItemText(0, _translate("ConsoleWindow", "--"))
        self.lineEndComboBox.setItemText(1, _translate("ConsoleWindow", "NL"))
        self.lineEndComboBox.setItemText(2, _translate("ConsoleWindow", "CR"))
        self.lineEndComboBox.setItemText(3, _translate("ConsoleWindow", "NL & CR"))
