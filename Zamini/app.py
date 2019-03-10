import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
from ui.mainform import *
from controls.init import *
from controls.control import *
from controls.funcRozklad import fillTable, addr_to_card,addr_to_dayPeriodTeach,id_to_card
from models.rozklad import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,\
                            QWidget, qApp

from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtCore import Qt, QModelIndex


#import controls.funcRozklad as fr
#import models.rozklad as rzkl



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
        #roz.periods_count = 8

        self.roz = Rozklad(r'2019_01_tmp_UTF-8.xml')

        self.roz.periods_count = len(self.roz.periods)


        fillTable(self, self.ui, self.ui.radioButton, self.roz)
        periods_count = len(self.roz.periods)


        self.roz.model = QStandardItemModel()
        list_init(self, self.roz.model)
        self.Dialog.listView.setModel(self.roz.model)
        self.ui.tableWidget.setMouseTracking(True)

        #Тут описуємо події
        self.ui.pushButton.clicked.connect(self.btn1_Click)
        self.ui.pushButton_2.clicked.connect(self.btn2_Click)
        self.ui.pushButton_3.clicked.connect(self.btn3_Click)
        self.ui.pushButton_4.clicked.connect(self.btn4_Click)
        self.ui.radioButton.clicked.connect(self.radioButton_Click)
        self.ui.radioButton_2.clicked.connect(self.radioButton_Click)

        self.ui.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.Dialog.listView.clicked.connect(self.list_click)


        #self.Dialog.listView.itemClicked.connect(self.item_clicked)

        #self.ui.tableWidget.cellEntered.connect(self.cellHover)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            print("pressed key " + str(event.key()))
            self.roz.lv_index = -1
            self.ui.pushButton_4.setText("")
            QApplication.setOverrideCursor(Qt.ArrowCursor)

    def cellHover (self, row, column):
        print ("========================")
        self.ui.tableWidget.setToolTip("")

    def list_click (self):
        # Запам'ятовуємо номер вибраного рядка
        self.roz.lv_index = self.Dialog.listView.selectedIndexes()[0].row()
        s = self.Dialog.listView.model().item(self.roz.lv_index).text()
        kl = ["", ""]
        kl = s.split("&")
        kl[0] = kl[0].rstrip()
        kl[1] = kl[1].rstrip()
        id = kl[1]
        card = id_to_card(self.roz, id)
        s = card.lesson.subjInThisLesson[0].short+"; " + \
            card.lesson.teacherInThisLesson[0].short
        self.Dialog.listView.setToolTip(s)

        self.ui.pushButton_4.setText(kl[0])
        #Встановлюємо підказку для вибраного рядка


        #self.ui.pushButton_4.setText("")
        # print ("======================== ", self.roz.lv_index)



    def eventFilter(self, source, event):
        print(event.type()," ")
        if (event.type() ==  QtCore.QEvent.MouseMove) and (source==self.ui.tableWidget):
            pos = event.pos()
            print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
        return True

    def cell_was_clicked(self, row, column):
        cell_clicked(self, self.roz, row, column) #Клацнули таблицю розкладу вчителів лівою кн. мишки




    def radioButton_Click(self):
        fillTable(self, self.ui, self.ui.radioButton, self.roz)

    def radioButton_2_Click(self):
        fillTable(self, self.ui, self.ui.radioButton, self.roz)

    def btn1_Click(self):
        self.ui.tableWidget2.setVisible(not self.ui.tableWidget2.isVisible())



    def btn2_Click(self):
        # if len(self.roz.model) > 0:

        # index = QModelIndex (self.Dialog.listView.index(0))
        self.Dialog.listView.setCurrentIndex(0)
        # self.roz.model.appendRow(QStandardItem("aaaaaaaaaaa"))   # Працює


    def btn3_Click(self):
        if self.Dialog.listView.model().rowCount() > 0:
            print("Вибрано елемент: ", self.Dialog.listView.selectedIndexes()[0].row())  # Працює
            print(self.Dialog.listView.model().item(0).text())  # Працює
            self.Dialog.listView.model().removeRows(0 , 1)  # Працює


    def item_clicked(item):
        #n = item.text()
        # value = self.Dialog.listWidget.model().data(0)

        #print(n)
        print("----")

    def btn4_Click(self):
        if  self.mode != "edit":
            self.ui.pushButton_4.setStyleSheet("font-weight: bold; background-color:yellow;")
            self.mode = "edit"
            self.Dialog.setGeometry(myapp.pos().x()+myapp.width()+5, myapp.pos().y()+27,110,myapp.height())
            # item = QtWidgets.QListWidgetItem(self.ui.pushButton_4.text())
            # self.Dialog.listWidget.addItem(item)
            # self.Dialog.listWidget.currentRow = 0
        else:
            self.mode = "view"
        self.roz.lv_index = (self.roz.model.rowCount()) - 1
        self.list_show()


    def list_show(self):
        self.Dialog.show()







if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()

    #Формуємо класи розкладу
    #roz_osnov = Rozklad(r'2019_01_tmp_UTF-8.xml')   # не змінений розклад
    # roz = Rozklad(r'2019_01_tmp_UTF-8.xml')
    #
    # roz.periods_count = len(roz.periods)
    # roz.model = []
    #
    #
    # fillTable(myapp.ui, roz)
    # periods_count = len(roz.periods)


    #print(addr_to_card( roz, "R4C4"))
    #print(addr_to_dayPeriodTeach(roz, "R4C4"))
    myapp.show()
    sys.exit(app.exec_())
