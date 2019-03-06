from PyQt5 import QtCore,  QtWidgets

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
            self.ui.pushButton_4.setText(item.text())
            s = cl.teacherInThisLesson[0].color
            r, g, b = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
        else:
            self.ui.pushButton_4.setText("")
            self.ui.label.setText("")

        self.ui.pushButton_4.setStyleSheet("background-color: rgb(" + str(r) + "," + str(g) + "," + str(b) + ")")