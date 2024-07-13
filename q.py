# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'questionarie.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(477, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 732, 357))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("margin-left: 100;\n"
"")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn2005 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.btn2005.setStyleSheet("")
        self.btn2005.setObjectName("btn2005")
        self.horizontalLayout_7.addWidget(self.btn2005)
        self.btn2010 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.btn2010.setStyleSheet("")
        self.btn2010.setObjectName("btn2010")
        self.horizontalLayout_7.addWidget(self.btn2010)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn2020 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.btn2020.setStyleSheet("")
        self.btn2020.setObjectName("btn2020")
        self.horizontalLayout_5.addWidget(self.btn2020)
        self.btn2015 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.btn2015.setStyleSheet("")
        self.btn2015.setObjectName("btn2015")
        self.horizontalLayout_5.addWidget(self.btn2015)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self._check_clicked()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Опитування від Crazy People"))
        self.label.setText(_translate("MainWindow", " Коли канал отримав золоту кнопку від Youtube?"))
        self.btn2005.setText(_translate("MainWindow", "2005"))
        self.btn2010.setText(_translate("MainWindow", "2010"))
        self.btn2020.setText(_translate("MainWindow", "2020"))
        self.btn2015.setText(_translate("MainWindow", "2015"))
    
    def _check_clicked(self):
        self.btn2005.clicked.connect(lambda: self._check_ans(self.btn2005))
        self.btn2010.clicked.connect(lambda: self._check_ans(self.btn2010))
        self.btn2015.clicked.connect(lambda: self._check_ans(self.btn2015))
        self.btn2020.clicked.connect(lambda: self._check_ans(self.btn2020))
    
    def _check_ans(self, button):
        if button == self.btn2015:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("You won!")
            msg.setText('Все правильно! Ви виграли гіроскутер!')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("You lose!")
            msg.setText('Ні, в 2015! Ви виграли фірмовий плакат!')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
