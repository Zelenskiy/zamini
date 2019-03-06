from PyQt5 import QtCore,  QtWidgets
from controls.funcRozklad import rowCol_to_dayPeriod, dayPeriodTeach_to_addr

def testFunc():
    print("Ok_1")

def testFunc2():
    print("Ok_2")

def cell_clicked(self, roz,row, column):
    # Вилучаємо вміст вибраної комірки
    if self.mode == "edit":
        print("sss  ", end="")
        #
        #   вилучаємо вміст
        k = self.ui.tableWidget.item(row, column)
        if k == None:
            k = ""
        else:
            k = k.text()
        print(k)
        kl = QtWidgets.QTableWidgetItem(self.oldClass)
        self.ui.tableWidget.setItem(row, column, kl)
        #   записуємо до комірки низ зписку
        if self.Dialog.listWidget.count() == 0:
            ss = self.Dialog.listWidget.currentRow()
            if ss != -1:
                kl = QtWidgets.QTableWidgetItem(ss)
                self.ui.tableWidget.setItem(row, column, kl)

                # !!!!!!!!!!!

        #   записуємо вилучене до низу списку
        if k != "":
            item = QtWidgets.QListWidgetItem(k)
            self.Dialog.listWidget.addItem(item)
            #TODO
            self.oldClass = item.text()
        else:
            self.oldClass = ""

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
            #TODO
            #self.ui.label.setToolTip("Some tooltip");
            day, period, teachId = rowCol_to_dayPeriod (roz, row, column)

            c = roz.dopTable.get(dayPeriodTeach_to_addr(roz, day, period, teachId))
            self.ui.label.setToolTip(c.subjInThisLesson[0].name+"\n"+ \
                                     c.classInThisLesson[0].name+"\n"+ \
                                     c.teacherInThisLesson[0].short)
            self.ui.tableWidget.setToolTip(c.subjInThisLesson[0].name+"\n"+ \
                                     c.classInThisLesson[0].name+"\n"+ \
                                     c.teacherInThisLesson[0].short);
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

