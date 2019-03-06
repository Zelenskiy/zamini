import sys

from ui.mainform import *
from controls.init import *
from controls.control import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,\
                            QWidget, qApp

from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtCore import Qt

import controls.funcRozklad as fr
import models.rozklad as rzkl



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
        self.periods_count = 8


        #Тут описуємо події
        self.ui.pushButton.clicked.connect(self.btn1_Click)
        self.ui.pushButton_2.clicked.connect(self.btn2_Click)
        self.ui.pushButton_4.clicked.connect(self.btn4_Click)
        self.ui.radioButton.clicked.connect(self.radioButton_Click)
        self.ui.radioButton_2.clicked.connect(self.radioButton_Click)


       # self.ui.tableWidget.mouseReleaseEvent = self.myMouseReleaseEvent
        #self.ui.tableWidget.mousePressEvent = self.mousePressEvent

        #self.ui.tableWidget.dragEnterEvent = self.dragEnterEvent
        #self.ui.tableWidget.dropEvent = self.myDropEvent
        #self.ui.tableWidget.startDrag = self.myStartDrag

        #self.ui.tableWidget.setMouseTracking(True)
        #self.ui.tableWidget.installEventFilter(self)

        self.ui.tableWidget.cellClicked.connect(self.cell_was_clicked)

        #self.ui.tableWidget.mouseMoveEvent = self.mouseMoveEvent

    def eventFilter(self, source, event):
        print(event.type()," ")
        if (event.type() ==  QtCore.QEvent.MouseMove) and (source==self.ui.tableWidget):
            pos = event.pos()
            print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
        return True

    def cell_was_clicked(self, row, column):
        cell_clicked(self, roz, row, column) #Клацнули таблицю розкладу вчителів лівою кн. мишки


    """
    def myDropEvent(self, event):
        print("myDropEvent (%s)" % event.pos())
        #super().DropEvent(event)
        super(self.ui.tableWidget).dropEvent(event)


    def myStartDrag(self, event):
        print("myStartDrag")

    def dropEvent(self, event):
        print("Закнчили тягнути")

    def myMouseReleaseEvent(self, event):
        print("Відпустили кнопку мишки")



    def mouseMoveEvent(self, event):

        if event.buttons() == QtCore.Qt.NoButton:
            print("Simple mouse motion", event.pos())

        elif event.buttons() == QtCore.Qt.LeftButton:
            print("Left click drag")
        elif event.buttons() == QtCore.Qt.RightButton:
            print  ("Right click drag")

        super()



    def table_Move(self):
        print("ssss")
    """

    def radioButton_Click(self):
        fr.fillTable(myapp.ui, roz)

    def radioButton_2_Click(self):
        fr.fillTable(myapp.ui, roz)

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







        # item = QtWidgets.QListWidgetItem("ss")
        # self.Dialog.listWidget.addItem (item)
        # self.Dialog.listWidget.addItem (item)
        # self.Dialog.listWidget.addItem (item)
        # self.Dialog.listWidget.addItem (item)
        # self.Dialog.listWidget.addItem (item)
        #Dialog.show()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()



    #Формуємо класи розкладу
    roz = rzkl.Rozklad(r'2019_01_tmp_UTF-8.xml')
    fr.fillTable(myapp.ui, roz)
    periods_count = len(roz.periods)



    myapp.show()
    sys.exit(app.exec_())
