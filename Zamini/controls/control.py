from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QApplication
from controls.funcRozklad import rowCol_to_dayPeriod, dayPeriodTeach_to_addr, rowCol_to_addr, addr_to_dayPeriodTeach, getForCard
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
        if tmp == None:
            tmp = ""
        else:
            tmp = tmp.text()
        # Записуємо до комірки значення зі списку
        # TODO

        self.ui.pushButton_4.setText(tmp)
        if roz.lv_index > -1:
            kl = QtWidgets.QTableWidgetItem(self.Dialog.listView.model().item(self.roz.lv_index).text())
        else:
            kl = QtWidgets.QTableWidgetItem("")
        self.ui.tableWidget.setItem(row, column, kl)
        #           проходимо по стовпчику і вилучаємо картки з даним класом до списку
        for r in range(0,len(roz.teachers)-1):
            if tmp != "":
                if self.ui.tableWidget.item(r, column) != None:
                    if self.ui.tableWidget.item(r, column).text() == tmp:
                        kl = QtWidgets.QTableWidgetItem("")
                        self.ui.tableWidget.setItem(r, column, kl)
                        roz.model.appendRow(QStandardItem(tmp))


        # Вилучаємо зі списку зчитане значення
        roz.model.removeRow(self.roz.lv_index)


        if self.roz.lv_index > roz.model.rowCount()-1:
            self.roz.lv_index = roz.model.rowCount() - 1
        if self.roz.lv_index > -1:
            tmp2 = self.Dialog.listView.model().item(self.roz.lv_index).text()
            self.ui.pushButton_4.setText(tmp2)
        # Записуємо до списку значення, яке на початку було в комірці
        if tmp != "":
            roz.model.appendRow(QStandardItem(tmp))

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




        """
        print("sss  ", end="")
        #
        #   вилучаємо вміст
        k = self.ui.tableWidget.item(row, column)
        if k == None:
            k = ""
        else:
            k = k.text()
            adr = rowCol_to_addr(roz, row, column)

            #tmpCard = getForCard(roz, day, period, teachId, weeks)
            #del roz.dopTable[adr]
        print(k)

        if k != "":
            pass
            roz.model.appendRow(QStandardItem(k))
            self.roz.lv_index = (roz.model.rowCount())-1    #ПРацює
        else:
            pass



        #
        if self.roz.lv_index > -1:
            kl = QtWidgets.QTableWidgetItem(self.Dialog.listView.model().item(self.roz.lv_index).text())
            #kl = QtWidgets.QTableWidgetItem(self.oldClass)
            self.ui.tableWidget.setItem(row, column, kl)
            roz.model.appendRow(QStandardItem(k))
            self.roz.lv_index = (roz.model.rowCount()) - 1  # ПРацює
        else:
            pass
        #   записуємо до комірки низ зписку
        # if self.Dialog.listView.count() == 0:
        #     ss = self.Dialog.listView.currentRow()
        #     if ss != -1:
        #         kl = QtWidgets.QTableWidgetItem(ss)
        #         self.ui.tableWidget.setItem(row, column, kl)


        #   записуємо вилучене до низу списку
        if k != "":
            item = QtWidgets.QListWidgetItem(k)
            # self.Dialog.listWidget.addItem(item)
            #TODO
            self.oldClass = item.text()
            #Запишемо на нове місце дану карточку
            adr = rowCol_to_addr(roz, row, column)
            day, period, teachId = addr_to_dayPeriodTeach(roz, adr)
            if (self.ui.radioButton.isChecked):
                weeks = "1"
            else:
                weeks = "01"

            roz.oldCard = getForCard(roz, day, period, teachId, weeks)

        else:
            self.oldClass = ""
        """
    else:
        print("Row %d and Column %d was clicked" % (row, column))
        r, g, b = 255, 255, 255
        item = self.ui.tableWidget.item(row, column)
        if item != None:
            cl = roz.dopTable.get("R" + str(row) + "C" + str(column))
            ls = ""
            for s in cl.subjInThisLesson:
                ls = ls + s.name
            self.ui.label.setText(ls)

            day, period, teachId = rowCol_to_dayPeriod (roz, row, column)

            c = roz.dopTable.get(dayPeriodTeach_to_addr(roz, day, period, teachId))

            self.ui.tableWidget.setToolTip(c.subjInThisLesson[0].short+"\n"+ \
                                     c.classInThisLesson[0].short+"\n"+ \
                                     c.teacherInThisLesson[0].short);



            #timer.start(1000)

            #print (c.lessonid)
            self.ui.pushButton_4.setText(item.text())
            s = cl.teacherInThisLesson[0].color
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

