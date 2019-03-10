from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QApplication
from controls.funcRozklad import rowCol_to_dayPeriod, dayPeriodTeach_to_addr, \
    rowCol_to_addr, addr_to_dayPeriodTeach, getForCard, id_to_card
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

def testFunc():
    print("Ok_1")

def testFunc2():
    print("Ok_2")




def cell_clicked(self, roz, row, column):

    if self.mode == "edit":
        #self.roz.lv_index = (roz.model.rowCount()) - 1

        # Записуємо значення комірки до тимчасової змінної
        # TODO
        #adrTmpRC = rowCol_to_addr(roz, row, column)

        tmp = self.ui.tableWidget.item(row, column)
        tmp2 = self.ui.tableWidget2.item(row, column)
        if tmp == None:
            tmp = ""
            tmp2 = ""
        else:
            tmp = tmp.text()
            tmp2 = tmp2.text()

        # Записуємо до комірки значення зі списку
        # TODO

        self.ui.pushButton_4.setText(tmp)
        kl = ["", ""]
        kli = ["", ""]
        if roz.lv_index > -1:
            klAll = QtWidgets.QTableWidgetItem(self.Dialog.listView.model().item(self.roz.lv_index).text())
            klAll = klAll.text()
            kl = klAll.split("&")
            kl[0] = kl[0].rstrip()
            kl[1] = kl[1].rstrip()

            kli[0] = QtWidgets.QTableWidgetItem(kl[0])
            kli[1] = QtWidgets.QTableWidgetItem(kl[1])
        else:
            kli[0] = QtWidgets.QTableWidgetItem("")
            kli[1] = QtWidgets.QTableWidgetItem("")
        self.ui.tableWidget.setItem(row, column, kli[0])
        self.ui.tableWidget2.setItem(row, column, kli[1])


        #           проходимо по стовпчику і вилучаємо картки з даним класом до списку
        for r in range(0, len(roz.teachers) - 1):
            if r == row:
                continue
            if kl[0] != "":
                if self.ui.tableWidget.item(r, column) != None:
                    s1 = self.ui.tableWidget.item(r, column).text()
                    if s1.strip() == kl[0].strip():
                        k_l = self.ui.tableWidget2.item(r, column)
                        if k_l == None:
                            k_l = ""
                        else:
                            k_l = k_l.text()
                        roz.model.appendRow(QStandardItem(kl[0]+"                        &"+k_l))
                        k_l = QtWidgets.QTableWidgetItem("")
                        self.ui.tableWidget.setItem(r, column, k_l)
                        self.ui.tableWidget2.setItem(r, column, k_l)



        # Вилучаємо зі списку зчитане значення
        roz.model.removeRow(self.roz.lv_index)


        if self.roz.lv_index > roz.model.rowCount()-1:
            self.roz.lv_index = roz.model.rowCount() - 1
        if self.roz.lv_index > -1:
            tmp2 = self.Dialog.listView.model().item(self.roz.lv_index).text()
            self.ui.pushButton_4.setText(tmp2)
        # Записуємо до списку значення, яке на початку було в комірці
        if tmp != "":
            roz.model.appendRow(QStandardItem(tmp+"                        &"+tmp2))
            self.roz.lv_index = (roz.model.rowCount()) - 1
        if roz.model.rowCount() > 0:
            # QApplication.setOverrideCursor(Qt.BitmapCursor)
            # bmp =

            # self.setCursor(QtGui.QCursor(QtGui.QPixmap("image.bmp"),0,0))
            QApplication.setOverrideCursor(Qt.DragMoveCursor)
            # QApplication.restoreOverrideCursor()
        else:

            QApplication.setOverrideCursor(Qt.ArrowCursor)
            # QApplication.restoreOverrideCursor()

    else:
        print("Row %d and Column %d was clicked" % (row, column))
        r, g, b = 255, 255, 255
        item = self.ui.tableWidget2.item(row, column)

        if item != None:
            cl = id_to_card(roz, item.text())
            ls = ""
            for s in cl.lesson.subjInThisLesson:
                ls = ls + s.name
            self.ui.label.setText(ls)

            day, period, teachId = rowCol_to_dayPeriod (roz, row, column)

            #c = roz.dopTable.get(dayPeriodTeach_to_addr(roz, day, period, teachId))

            self.ui.tableWidget.setToolTip(cl.lesson.subjInThisLesson[0].short+"\n"+ \
                                     cl.lesson.classInThisLesson[0].short+"\n"+ \
                                     cl.lesson.teacherInThisLesson[0].short);



            #timer.start(1000)

            #print (c.lessonid)
            self.ui.pushButton_4.setText(item.text())
            s = cl.lesson.teacherInThisLesson[0].color
            r, g, b = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
        else:
            self.ui.pushButton_4.setText("")
            self.ui.label.setText("")
            self.ui.label.setToolTip("")
            self.ui.tableWidget.setToolTip("")

        self.ui.pushButton_4.setStyleSheet("background-color: rgb(" + str(r) + "," + str(g) + "," + str(b) + ")")



        # self.ui.tableWidget.mouseReleaseEvent = self.myMouseReleaseEvent
        #self.ui.tableWidget.mousePressEvent = self.mousePressEvent

        #self.ui.tableWidget.dragEnterEvent = self.dragEnterEvent
        #self.ui.tableWidget.dropEvent = self.myDropEvent
        #self.ui.tableWidget.startDrag = self.myStartDrag

        #self.ui.tableWidget.setMouseTracking(True)
        #self.ui.tableWidget.installEventFilter(self)
        # self.ui.tableWidget.mouseMoveEvent = self.mouseMoveEvent



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

    # item = QtWidgets.QListWidgetItem("ss")
    # self.Dialog.listWidget.addItem (item)
    # self.Dialog.listWidget.addItem (item)
    # self.Dialog.listWidget.addItem (item)
    # self.Dialog.listWidget.addItem (item)
    # self.Dialog.listWidget.addItem (item)
    # Dialog.show()

