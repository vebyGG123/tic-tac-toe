###################   
#                 #
#                 #
# KRESTIKI_NOLIKI #
#     BY VEBY     #
#   TG:@vebytop   #
#                 #
###################


from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
import sys



class Ui_Krestiki_Noliki(object):
    kres_nolik = 0
    pobeda_krestikov = 0
    pobeda_nolikov = 0
    nichai = 0


    def setupUi(self, Krestiki_Noliki):
        Krestiki_Noliki.setObjectName("Krestiki_Noliki")
        Krestiki_Noliki.resize(400, 312)
        Krestiki_Noliki.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Krestiki_Noliki)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 161, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(246, 144, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(183, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(247, 208, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 170, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 144, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(246, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(183, 144, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 208, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(183, 208, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(3, 112, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1, 283, 171, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(216, 284, 191, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        Krestiki_Noliki.setCentralWidget(self.centralwidget)

        self.retranslateUi(Krestiki_Noliki)
        QtCore.QMetaObject.connectSlotsByName(Krestiki_Noliki)

        self.correct_button()

    
    def correct_button(self):
        self.pushButton.clicked.connect(self.main_1)
        self.pushButton_2.clicked.connect(self.main_2)
        self.pushButton_3.clicked.connect(self.main_3)
        self.pushButton_4.clicked.connect(self.main_4)
        self.pushButton_5.clicked.connect(self.main_5)
        self.pushButton_6.clicked.connect(self.main_6)
        self.pushButton_7.clicked.connect(self.main_7)
        self.pushButton_8.clicked.connect(self.main_8)
        self.pushButton_9.clicked.connect(self.main_9)
        self.pushButton_10.clicked.connect(self.resyltat)
        self.pushButton_11.clicked.connect(self.zbros_resyltat)


    def zbros_resyltat(self):
        messagebox.showinfo("Уведомление!", "Результат cброшен!")
        self.pobeda_krestikov = 0
        self.pobeda_nolikov = 0
        self.nichai = 0


    def resyltat(self):
        messagebox.showinfo("Результаты!", f"Победы крестиков: {self.pobeda_krestikov}")
        messagebox.showinfo("Результаты!", f"Победы ноликов: {self.pobeda_nolikov}")
        messagebox.showinfo("Результаты!", f"Ничья: {self.nichai}")


    def main_1(self):
        self.kres_nolik += 1
        if self.kres_nolik % 2 == 0:
            self.pushButton.setText("O")
            self.label_6.setText("Ходят: крестики")
        else:
            self.pushButton.setText("X")
            self.label_6.setText("Ходят: нолики")

        self.pushButton.setEnabled(False)
        self.check_finaly()

    def main_2(self):
        self.kres_nolik += 1
        if self.kres_nolik % 2 == 0:
            self.pushButton_2.setText("O")
            self.label_6.setText("Ходят: крестики")
        else:
            self.pushButton_2.setText("X")
            self.label_6.setText("Ходят: нолики")

        self.pushButton_2.setEnabled(False)
        self.check_finaly()

    def main_3(self):
        self.kres_nolik += 1
        if self.kres_nolik % 2 == 0:
            self.pushButton_3.setText("O")
            self.label_6.setText("Ходят: крестики")
        else:
            self.pushButton_3.setText("X")
            self.label_6.setText("Ходят: нолики")

        self.pushButton_3.setEnabled(False)
        self.check_finaly()

    def main_4(self):
        self.kres_nolik += 1
        if self.kres_nolik % 2 == 0:
            self.pushButton_4.setText("O")
            self.label_6.setText("Ходят: крестики")
        else:
            self.pushButton_4.setText("X")
            self.label_6.setText("Ходят: нолики")

        self.pushButton_4.setEnabled(False)
        self.check_finaly()

    def main_5(self):
        self.kres_nolik += 1
        if self.kres_nolik % 2 == 0:
            self.pushButton_5.setText("O")
            self.label_6.setText("Ходят: крестики")
        else:
            self.pushButton_5.setText("X")
            self.label_6.setText("Ходят: нолики")

        self.pushButton_5.setEnabled(False)
        self.check_finaly()

    def main_6(self):
        self.kres_nolik += 1
        if self.kres_nolik % 2 == 0:
            self.pushButton_6.setText("O")
            self.label_6.setText("Ходят: крестики")
        else:
            self.pushButton_6.setText("X")
            self.label_6.setText("Ходят: нолики")

        self.pushButton_6.setEnabled(False)
        self.check_finaly()

    def main_7(self):
        self.kres_nolik += 1
        if self.kres_nolik % 2 == 0:
            self.pushButton_7.setText("O")
            self.label_6.setText("Ходят: крестики")

        else:
            self.pushButton_7.setText("X")
            self.label_6.setText("Ходят: нолики")

        self.pushButton_7.setEnabled(False)
        self.check_finaly()

    def main_8(self):
        self.kres_nolik += 1
        if self.kres_nolik % 2 == 0:
            self.pushButton_8.setText("O")
            self.label_6.setText("Ходят: крестики")
        else:
            self.pushButton_8.setText("X")
            self.label_6.setText("Ходят: нолики")

        self.pushButton_8.setEnabled(False)
        self.check_finaly()

    def main_9(self):
        self.kres_nolik += 1
        if self.kres_nolik % 2 == 0:
            self.pushButton_9.setText("O")
            self.label_6.setText("Ходят: крестики")
        else:
            self.pushButton_9.setText("X")
            self.label_6.setText("Ходят: нолики")

        self.pushButton_9.setEnabled(False)
        self.check_finaly()

    
    def check_finaly(self):
        text_1 = self.pushButton.text()
        text_2 = self.pushButton_2.text()
        text_3 = self.pushButton_3.text()
        text_4 = self.pushButton_4.text()
        text_5 = self.pushButton_5.text()
        text_6 = self.pushButton_6.text()
        text_7 = self.pushButton_7.text()
        text_8 = self.pushButton_8.text()
        text_9 = self.pushButton_9.text()

        check_pobeda = False

        if text_1 and text_5 and text_8 != "":
            if text_1 == text_5 == text_8:
                if text_1 == "X":
                    messagebox.showinfo("Результат!", "Выйграли крестики!")
                    self.pobeda_krestikov += 1
                else:
                    messagebox.showinfo("Результат!", "Выйграли нолики!")
                    self.pobeda_nolikov += 1

                check_pobeda = True
                self.kres_nolik = 0
                self.label_6.setText("Ходят: крестики")

                self.pushButton.setText("")
                self.pushButton_2.setText("")
                self.pushButton_3.setText("")
                self.pushButton_4.setText("")
                self.pushButton_5.setText("")
                self.pushButton_6.setText("")
                self.pushButton_7.setText("")
                self.pushButton_8.setText("")
                self.pushButton_9.setText("")

                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.pushButton_9.setEnabled(True)

        if text_1 and text_3 and text_6 != "":
            if text_1 == text_3 == text_6:
                if text_1 == "X":
                    messagebox.showinfo("Результат!", "Выйграли крестики!")
                    self.pobeda_krestikov += 1
                else:
                    messagebox.showinfo("Результат!", "Выйграли нолики!")
                    self.pobeda_nolikov += 1

                check_pobeda = True
                self.kres_nolik = 0
                self.label_6.setText("Ходят: крестики")

                self.pushButton.setText("")
                self.pushButton_2.setText("")
                self.pushButton_3.setText("")
                self.pushButton_4.setText("")
                self.pushButton_5.setText("")
                self.pushButton_6.setText("")
                self.pushButton_7.setText("")
                self.pushButton_8.setText("")
                self.pushButton_9.setText("")
                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.pushButton_9.setEnabled(True)

        if text_1 and text_7 and text_4 != "":
            if text_1 == text_7 == text_4:
                if text_1 == "X":
                    messagebox.showinfo("Результат!", "Выйграли крестики!")
                    self.pobeda_krestikov += 1
                else:
                    messagebox.showinfo("Результат!", "Выйграли нолики!")
                    self.pobeda_nolikov += 1

                check_pobeda = True
                self.kres_nolik = 0
                self.label_6.setText("Ходят: крестики")

                self.pushButton.setText("")
                self.pushButton_2.setText("")
                self.pushButton_3.setText("")
                self.pushButton_4.setText("")
                self.pushButton_5.setText("")
                self.pushButton_6.setText("")
                self.pushButton_7.setText("")
                self.pushButton_8.setText("")
                self.pushButton_9.setText("")

                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.pushButton_9.setEnabled(True)

        if text_3 and text_7 and text_9 != "":
            if text_3 == text_7 == text_9:
                if text_3 == "X":
                    messagebox.showinfo("Результат!", "Выйграли крестики!")
                    self.pobeda_krestikov += 1
                else:
                    messagebox.showinfo("Результат!", "Выйграли нолики!")
                    self.pobeda_nolikov += 1

                check_pobeda = True
                self.kres_nolik = 0
                self.label_6.setText("Ходят: крестики")

                self.pushButton.setText("")
                self.pushButton_2.setText("")
                self.pushButton_3.setText("")
                self.pushButton_4.setText("")
                self.pushButton_5.setText("")
                self.pushButton_6.setText("")
                self.pushButton_7.setText("")
                self.pushButton_8.setText("")
                self.pushButton_9.setText("")

                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.pushButton_9.setEnabled(True)

        if text_6 and text_7 and text_8 != "":
            if text_6 == text_7 == text_8:
                if text_6 == "X":
                    messagebox.showinfo("Результат!", "Выйграли крестики!")
                    self.pobeda_krestikov += 1
                else:
                    messagebox.showinfo("Результат!", "Выйграли нолики!")
                    self.pobeda_nolikov += 1

                check_pobeda = True
                self.kres_nolik = 0
                self.label_6.setText("Ходят: крестики")


                self.pushButton.setText("")
                self.pushButton_2.setText("")
                self.pushButton_3.setText("")
                self.pushButton_4.setText("")
                self.pushButton_5.setText("")
                self.pushButton_6.setText("")
                self.pushButton_7.setText("")
                self.pushButton_8.setText("")
                self.pushButton_9.setText("")

                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.pushButton_9.setEnabled(True)

        if text_6 and text_2 and text_4 != "":
            if text_6 == text_2 == text_4:
                if text_6 == "X":
                    messagebox.showinfo("Результат!", "Выйграли крестики!")
                    self.pobeda_krestikov += 1
                else:
                    messagebox.showinfo("Результат!", "Выйграли нолики!")
                    self.pobeda_nolikov += 1


                self.label_6.setText("Ходят: крестики")
                check_pobeda = True
                self.kres_nolik = 0

                self.pushButton.setText("")
                self.pushButton_2.setText("")
                self.pushButton_3.setText("")
                self.pushButton_4.setText("")
                self.pushButton_5.setText("")
                self.pushButton_6.setText("")
                self.pushButton_7.setText("")
                self.pushButton_8.setText("")
                self.pushButton_9.setText("")

                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.pushButton_9.setEnabled(True)

        if text_5 and text_7 and text_2 != "":
            if text_5 == text_7 == text_2:
                if text_5 == "X":
                    messagebox.showinfo("Результат!", "Выйграли крестики!")
                    self.pobeda_krestikov += 1
                else:
                    messagebox.showinfo("Результат!", "Выйграли нолики!")
                    self.pobeda_nolikov += 1

                    
                self.label_6.setText("Ходят: крестики")
                check_pobeda = True
                self.kres_nolik = 0

                self.pushButton.setText("")
                self.pushButton_2.setText("")
                self.pushButton_3.setText("")
                self.pushButton_4.setText("")
                self.pushButton_5.setText("")
                self.pushButton_6.setText("")
                self.pushButton_7.setText("")
                self.pushButton_8.setText("")
                self.pushButton_9.setText("")

                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.pushButton_9.setEnabled(True)

        if text_8 and text_9 and text_4 != "":
            if text_8 == text_9 == text_4:
                if text_8 == "X":
                    messagebox.showinfo("Результат!", "Выйграли крестики!")
                    self.pobeda_krestikov += 1
                else:
                    messagebox.showinfo("Результат!", "Выйграли нолики!")
                    self.pobeda_nolikov += 1


                self.label_6.setText("Ходят: крестики")
                check_pobeda = True
                self.kres_nolik = 0

                self.pushButton.setText("")
                self.pushButton_2.setText("")
                self.pushButton_3.setText("")
                self.pushButton_4.setText("")
                self.pushButton_5.setText("")
                self.pushButton_6.setText("")
                self.pushButton_7.setText("")
                self.pushButton_8.setText("")
                self.pushButton_9.setText("")

                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.pushButton_9.setEnabled(True)


        if self.kres_nolik == 9 and check_pobeda == False:
            messagebox.showinfo("Результат!", "Ничья!")
            self.label_6.setText("Ходят: крестики")
            self.nichai += 1
            self.kres_nolik = 0

            self.pushButton.setText("")
            self.pushButton_2.setText("")
            self.pushButton_3.setText("")
            self.pushButton_4.setText("")
            self.pushButton_5.setText("")
            self.pushButton_6.setText("")
            self.pushButton_7.setText("")
            self.pushButton_8.setText("")
            self.pushButton_9.setText("")

            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_6.setEnabled(True)
            self.pushButton_7.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            self.pushButton_9.setEnabled(True)



    def retranslateUi(self, Krestiki_Noliki):
        _translate = QtCore.QCoreApplication.translate
        Krestiki_Noliki.setWindowTitle(_translate("Krestiki_Noliki", "MainWindow"))
        self.label.setText(_translate("Krestiki_Noliki", "Разработчик: Veby, TG: @vebytop."))
        self.label_2.setText(_translate("Krestiki_Noliki", "Игра крестики нолики"))
        self.label_6.setText(_translate("Krestiki_Noliki", "Ходят: крестики"))
        self.pushButton_10.setText(_translate("Krestiki_Noliki", "Показать результаты!"))
        self.pushButton_11.setText(_translate("Krestiki_Noliki", "Cбросить результат!"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Krestiki_Noliki()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())