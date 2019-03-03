import sys

from ui.mainform import *
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
        self.list_init()

        self.ui.radioButton.setChecked(True)

        self.mode = "view"

        #self.list_init()

        #self.ui.tableWidget.setDragEnabled(True)
        #self.ui.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)


        # self.ui.tableWidget.setMouseTracking(True) #Щоб спрацьовувало при ненатиснутій кнопці

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
        # Вилучаємо вміст вибраної комірки
        if self.mode == "edit":
            print("sss")
            #

            #   вилучаємо вміст
            k = self.ui.tableWidget.item(row, column).text()
            kl = QtWidgets.QTableWidgetItem("")
            self.ui.tableWidget.setItem(row, column, kl)
            #   записуємо до комірки низ зписку
            if self.Dialog.listWidget.count()==0:
                ss = self.Dialog.listWidget.currentRow()
                if ss!=-1:
                    kl = QtWidgets.QTableWidgetItem(ss)
                    self.ui.tableWidget.setItem(row, column, kl)

            #   записуємо вилучене до низу списку
            item = QtWidgets.QListWidgetItem(k)
            self.Dialog.listWidget.addItem(item)



        else:
            print("Row %d and Column %d was clicked" % (row, column))
            r, g, b = 255, 255, 255
            item = self.ui.tableWidget.item(row, column)
            if item != None:
                cl = roz.dopTable.get("R"+str(row)+"C"+str(column))
                ls = ""
                for s in cl.subjInThisLesson:
                    ls = ls + s.name
                self.ui.label.setText(ls)
                self.ui.pushButton_4.setText(item.text())
                s = cl.teacherInThisLesson[0].color
                r, g, b = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
            else:
                self.ui.pushButton_4.setText("")
                self.ui.label.setText("")


            self.ui.pushButton_4.setStyleSheet("background-color: rgb("+str(r)+","+str(g)+","+str(b)+")")

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

    def radioButton_Click(self):
        fr.fillTable(myapp.ui, roz)

    def radioButton_2_Click(self):
        fr.fillTable(myapp.ui, roz)

    def btn1_Click(self):
        #self.list_show()
        print("")

    def btn2_Click(self):
        print("")

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

    def list_init(self):
        self.Dialog.resize(265, 300)
        self.Dialog.verticalLayout = QtWidgets.QVBoxLayout(self.Dialog)
        self.Dialog.verticalLayout.setObjectName("verticalLayout")
        self.Dialog.listWidget = QtWidgets.QListWidget(self.Dialog)
        self.Dialog.listWidget.setObjectName("listWidget")
        self.Dialog.horizontalLayout = QtWidgets.QHBoxLayout()
        self.Dialog.verticalLayout.addWidget(self.Dialog.listWidget)

        self.Dialog.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Dialog.horizontalLayout.addItem(spacerItem)
        self.Dialog.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.Dialog.pushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.Dialog.pushButton.setObjectName("pushButton")
        self.Dialog.horizontalLayout.addWidget(self.Dialog.pushButton)
        self.Dialog.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.Dialog.pushButton_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.Dialog.pushButton_2.setObjectName("pushButton_2")
        self.Dialog.horizontalLayout.addWidget(self.Dialog.pushButton_2)
        self.Dialog.verticalLayout.addLayout(self.Dialog.horizontalLayout)

        self.Dialog.pushButton.setText("1")
        self.Dialog.pushButton_2.setText("2")




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




    myapp.show()
    sys.exit(app.exec_())
