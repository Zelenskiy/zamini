import sys

from ui.mainform import *
from controls.init import *
from controls.control import *
from controls.funcRozklad import fillTable, addr_to_card,addr_to_dayPeriodTeach
from models.rozklad import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,\
                            QWidget, qApp

from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtCore import Qt

#import controls.funcRozklad as fr
#import models.rozklad as rzkl



class MyWin(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Dialog = QWidget(self, Qt.Window)
        list_init(self)

        self.ui.radioButton.setChecked(True)

        self.mode = "view"
        self.oldClass = ""
        #roz.periods_count = 8


        #Тут описуємо події
        self.ui.pushButton.clicked.connect(self.btn1_Click)
        self.ui.pushButton_2.clicked.connect(self.btn2_Click)
        self.ui.pushButton_4.clicked.connect(self.btn4_Click)
        self.ui.radioButton.clicked.connect(self.radioButton_Click)
        self.ui.radioButton_2.clicked.connect(self.radioButton_Click)



        self.ui.tableWidget.cellClicked.connect(self.cell_was_clicked)



    def eventFilter(self, source, event):
        print(event.type()," ")
        if (event.type() ==  QtCore.QEvent.MouseMove) and (source==self.ui.tableWidget):
            pos = event.pos()
            print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
        return True

    def cell_was_clicked(self, row, column):
        cell_clicked(self, roz, row, column) #Клацнули таблицю розкладу вчителів лівою кн. мишки




    def radioButton_Click(self):
        fillTable(myapp.ui, roz)

    def radioButton_2_Click(self):
        fillTable(myapp.ui, roz)

    def btn1_Click(self):
        #self.list_show()
        print("")

    def btn2_Click(self):
        print("")

    def item_clicked(item):
        #n = item.text()
        # value = self.Dialog.listWidget.model().data(0)

        #print(n)
        print("----")

    def btn4_Click(self):
        self.ui.pushButton_4.setStyleSheet("font-weight: bold; background-color:yellow;")
        self.mode = "edit"
        self.Dialog.setGeometry(myapp.pos().x()+myapp.width()+5, myapp.pos().y()+27,300,myapp.height())
        item = QtWidgets.QListWidgetItem(self.ui.pushButton_4.text())
        self.Dialog.listWidget.addItem(item)
        self.Dialog.listWidget.currentRow = 0

        self.list_show()
        print("44444")

    def list_show(self):
        self.Dialog.show()







if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()

    #Формуємо класи розкладу
    roz = Rozklad(r'2019_01_tmp_UTF-8.xml')
    roz.periods_count = len(roz.periods)
    fillTable(myapp.ui, roz)
    periods_count = len(roz.periods)
    print(addr_to_card( roz, "R4C4"))
    print(addr_to_dayPeriodTeach(roz, "R4C4"))
    myapp.show()
    sys.exit(app.exec_())
