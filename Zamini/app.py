import sys

# from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, \
    QWidget, qApp, QListWidgetItem

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QModelIndex

from ui.mainform import *
from controls.control import *
from controls.funcRozklad import *
from models.rozklad import *


# import controls.funcRozklad as fr
# import models.rozklad as rzkl


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Dialog = QWidget(self, Qt.Window)
        self.whatEverColor = QColor(Qt.white)

        self.ui.radioButton.setChecked(True)

        self.mode = "view"
        self.oldClass = ""
        self.boxCards = []
        # roz.periods_count = 8

        self.roz = Rozklad(r'2019_03_08_utf.xml')

        self.roz.periods_count = len(self.roz.periods)

        fillTable(self, self.ui, self.roz)
        periods_count = len(self.roz.periods)

        self.roz.model = QStandardItemModel()

        # list_init(self, self.roz.model)

        self.ui.listView.setModel(self.roz.model)
        self.ui.tableWidget.setMouseTracking(True)

        # Тут описуємо події
        self.ui.pushButton.clicked.connect(self.btn1_Click)
        self.ui.pushButton_2.clicked.connect(self.btn2_Click)
        self.ui.pushButton_3.clicked.connect(self.btn3_Click)
        self.ui.pushButton_4.clicked.connect(self.btn4_Click)
        self.ui.pushButton_7.clicked.connect(self.btn7_Click)
        self.ui.pushButton_8.clicked.connect(self.btn8_Click)
        self.ui.pushButton_6.clicked.connect(self.btn6_Click)



        self.ui.radioButton.clicked.connect(self.radioButton_Click)
        self.ui.radioButton_2.clicked.connect(self.radioButton_2_Click)

        # self.ui.tableWidget.mousePressEvent = self.mousePressEvent
        # self.ui.tableWidget.mouseReleaseEvent = self.mouseReleaseEvent

        self.ui.tableWidget.cellClicked.connect(self.cell_was_clicked)


        self.ui.listView.clicked.connect(self.list_click)
        # self.ui.listView.paintEvent = self.paintEvent


        self.ui.comboBox.activated.connect(self.comboBox_click)

        # self.Dialog.listView.itemClicked.connect(self.item_clicked)

        # self.ui.tableWidget.cellEntered.connect(self.cellHover)

        self.ui.scrollArea_2.setVisible(False)
        self.ui.tableWidget2.setVisible(False)

    # def paintEvent(self,event):
    #     print ("paintEvent")

    # def mousePressEvent(self, event):
    #     super().mousePressEvent(event)
    #     if event.buttons() == Qt.LeftButton:
    #         print ("left")
    #     else:
    #         print("right")

    #
    # def mouseReleaseEvent(self, event):
    #     if event.buttons() == Qt.LeftButton:
    #         print("left")
    #     else:
    #         print("right")
    #
    #     super().mouseReleaseEvent(event)
    #     cell_clicked(self, self.roz)

    # if event.buttons() == Qt.LeftButton:
    #     cell_clicked(self, self.roz)

    def comboBox_click(self):
        # Вибираємо уроки відсутнього вчителя
        print(self.ui.comboBox.currentText())  # Працює
        # Виділяємо вчителя в таблиці

        self.ui.tableWidget.item(1, 0).setBackground(QColor(100, 100, 150))

        for i in range(0, 10):
            if self.ui.tableWidget.item(1, i) != None:
                self.ui.tableWidget.item(1, i).setBackground(QColor(100, 50, 150))



    def cell_was_clicked(self, row, column):
        # print ("hohohohoho")
        # print(row, "   ", column)
        cell_clicked(self, self.roz, row, column)  # Клацнули таблицю розкладу вчителів лівою кн. мишки

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            print("pressed key " + str(event.key()))
            self.roz.lv_index = -1
            self.ui.pushButton_4.setText("")
            QApplication.setOverrideCursor(Qt.ArrowCursor)

    def cellHover(self, row, column):
        print("========================")
        self.ui.tableWidget.setToolTip("")

    def list_click(self):
        # Запам'ятовуємо номер вибраного рядка
        self.roz.lv_index = self.ui.listView.selectedIndexes()[0].row()
        s = self.ui.listView.model().item(self.roz.lv_index).text()
        kl = ["", ""]
        kl = s.split("&")
        kl[0] = kl[0].rstrip()
        kl[1] = kl[1].rstrip()
        id = kl[1]
        card = id_to_card(self.roz, id)
        s = card.lesson.subjInThisLesson[0].short + "; " + \
            card.lesson.teacherInThisLesson[0].short
        self.ui.listView.setToolTip(s)

        self.ui.pushButton_4.setText(kl[0])
        mySetCursor(self, kl[0])
        # Встановлюємо підказку для вибраного рядка

        # self.ui.pushButton_4.setText("")
        # print ("======================== ", self.roz.lv_index)

    def eventFilter(self, source, event):
        print(event.type(), " ")
        if (event.type() == QtCore.QEvent.MouseMove) and (source == self.ui.tableWidget):
            pos = event.pos()
            print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
        return True

    def radioButton_Click(self):
        fillTable(self, self.ui, self.roz)

    def radioButton_2_Click(self):
        fillTable(self, self.ui, self.roz)

    def btn1_Click(self):
        self.ui.tableWidget2.setVisible(not self.ui.tableWidget2.isVisible())

    def btn6_Click(self):
        print("=============")
        print(self.ui.listWidget.item(self.ui.listWidget.currentRow()).text())

        # for item in range(self.ui.listWidget.count()):
        #     print(self.ui.listWidget.item(item).text())


    def btn8_Click(self):
        if self.ui.listWidget.selectedItems() != []:
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())


    def btn7_Click(self):
        if self.ui.comboBox.currentText() != "-------":
            item = QListWidgetItem(self.ui.comboBox.currentText())
            it = self.ui.listWidget.findItems(self.ui.comboBox.currentText(), Qt.MatchExactly)
            if len(it) == 0:
                self.ui.listWidget.addItem(item)


    def btn2_Click(self):
        for c in self.roz.cards:
            # print(c.id)
            if str(c.id) == '*17':
                print(c.lesson.classInThisLesson[0].short)
                c.lesson.classInThisLesson[0].short = "qqq"
                print(c.lesson.classInThisLesson[0].short)
                break



    def btn3_Click(self):
        if self.ui.listView.model().rowCount() > 0:
            print("Вибрано елемент: ", self.Dialog.listView.selectedIndexes()[0].row())  # Працює
            print(self.ui.listView.model().item(0).text())  # Працює
            self.ui.listView.model().removeRows(0, 1)  # Працює

    def item_clicked(item):
        # n = item.text()
        # value = self.Dialog.listWidget.model().data(0)

        # print(n)
        print("----")

    def btn4_Click(self):
        if self.mode != "edit":
            self.ui.pushButton_4.setStyleSheet("font-weight: bold; background-color:yellow;")
            self.mode = "edit"
            self.ui.scrollArea_2.setVisible(True)
            # self.Dialog.setGeometry(myapp.pos().x()+myapp.width()+5, myapp.pos().y()+27,110,myapp.height())
            # item = QtWidgets.QListWidgetItem(self.ui.pushButton_4.text())
            # self.Dialog.listWidget.addItem(item)
            # self.Dialog.listWidget.currentRow = 0
        else:
            self.mode = "view"
            self.ui.scrollArea_2.setVisible(False)
            QApplication.setOverrideCursor(Qt.ArrowCursor)
        self.roz.lv_index = (self.roz.model.rowCount()) - 1

    def list_show(self):
        self.ui.listView.setVisible(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()

    # Формуємо класи розкладу
    # roz_osnov = Rozklad(r'2019_01_tmp_UTF-8.xml')   # не змінений розклад
    # roz = Rozklad(r'2019_01_tmp_UTF-8.xml')
    #
    # roz.periods_count = len(roz.periods)
    # roz.model = []
    #
    #
    # fillTable(myapp.ui, roz)
    # periods_count = len(roz.periods)

    # print(addr_to_card( roz, "R4C4"))
    # print(addr_to_dayPeriodTeach(roz, "R4C4"))
    myapp.show()
    sys.exit(app.exec_())
