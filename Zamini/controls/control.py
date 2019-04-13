from PyQt5 import QtCore, QtWidgets, QtGui

# from PyQt5 import QStandardItem, QPainter, QFont, QColor
from PyQt5.QtCore import QPoint, QRect, QItemSelectionModel, Qt
from PyQt5.QtGui import QStandardItem, QPixmap, QPainter, QColor, QFont

from controls.funcRozklad import card_to_tip, rowCol_to_dayPeriodTeacher, id_to_card
# from Zamini.controls.funcRozklad import card_to_tip, rowCol_to_dayPeriodTeacher


def testFunc():
    print("Ok_1")


def testFunc2():
    print("Ok_2")

    """
    procedure DrawArrowHead(Canvas: TCanvas; X, Y: integer; Angle, LW: extended);
var
  A1, A2: extended;
  Arrow: array[0..3] of TPoint;
  OldWidth: integer;
const
  Beta = 0.322;
  LineLen = 4.74;
  CentLen = 3;
begin
  Angle := Pi + Angle;
  Arrow[0] := Point(X, Y);
  A1 := Angle - Beta;
  A2 := Angle + Beta;
  Arrow[1] := Point(X + Round(LineLen * LW * Cos(A1)), Y - Round(LineLen * LW * Sin(A1)));
  Arrow[2] := Point(X + Round(CentLen * LW * Cos(Angle)), Y - Round(CentLen * LW * Sin(Angle)));
  Arrow[3] := Point(X + Round(LineLen * LW * Cos(A2)), Y - Round(LineLen * LW * Sin(A2)));
  OldWidth := Canvas.Pen.Width;
  Canvas.Pen.Width := 1;
  Canvas.Brush.Style := bsSolid;
  Canvas.Pen.Color := Form1.penColor;
  Canvas.Brush.Color := Form1.penColor;
  Canvas.Polygon(Arrow);
  Canvas.Pen.Width := OldWidth;
end;
    
    """
# sdafasdfasdf

def mySetCursor(self, text):
    if text != "":
        bmp = QPixmap(32, 32)
        bmp.fill()
        qp = QPainter()
        qp.begin(bmp)
        qp.setPen(QtGui.QPen(QtGui.QColor("#000"), 2, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap))

        polygon = QtGui.QPolygonF()
        polygon.append(QtCore.QPointF(0, 0))
        polygon.append(QtCore.QPointF(16, 8))
        polygon.append(QtCore.QPointF(8, 8))
        polygon.append(QtCore.QPointF(8, 16))
        polygon.append(QtCore.QPointF(0, 0))

        qp.drawPolygon(polygon)
        qp.setPen(QColor(0, 0, 255))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(QRect(0, 0, 32, 32), Qt.AlignCenter, text)

        qp.end()
        qp.drawPixmap(QPoint(0, 0), bmp, QRect(0, 0, 32, 32))
        self.ui.tableWidget.setCursor(QtGui.QCursor(bmp, 0, 0))

    else:
        self.ui.tableWidget.setCursor(Qt.ArrowCursor)
        # QApplication.setOverrideCursor(Qt.ArrowCursor)


# Вилучаємо вміст комірки в таблицях
def cell_remove(self, row, column):
    self.ui.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(""))
    self.ui.tableWidget2.setItem(row, column, QtWidgets.QTableWidgetItem(""))


# Вилучаємо картку з обох таблиць
def card_remove(self, card):
    if card != None:
        for r in range(0, self.ui.tableWidget.rowCount()):
            for c in range(0, self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget2.item(r, c)
                if item != None:
                    item = item.text()
                    if item == card.id:
                        self.ui.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(""))
                        self.ui.tableWidget2.setItem(r, c, QtWidgets.QTableWidgetItem(""))


# Беремо вміст комірок з таблиць
def cell_to_card(self, row, column):
    klas = self.ui.tableWidget.item(row, column)

    if klas == None:
        klas = ""
    else:
        klas = klas.text()
    id_card = self.ui.tableWidget2.item(row, column)
    if id_card == None:
        id_card = ""
    else:
        id_card = id_card.text()
    card = id_to_card(self.roz, id_card)
    return klas, card


# Записуємо до комірок таблиць та замінюємо там поля day period
def card_to_cell(self, card, row, column):
    if card == None:
        self.ui.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(""))
        self.ui.tableWidget2.setItem(row, column, QtWidgets.QTableWidgetItem(""))
    else:
        cl = ""
        for c in card.lesson.classInThisLesson:
            cl += c.short + " "
        cl = cl.strip()
        t = QtWidgets.QTableWidgetItem(cl)
        self.ui.tableWidget.setItem(row, column, t)
        self.ui.tableWidget2.setItem(row, column, QtWidgets.QTableWidgetItem(card.id))
        s = card.lesson.teacherInThisLesson[0].color
        r, g, b = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
        self.ui.tableWidget.item(row, column).setBackground(QtGui.QColor(r, g, b))

        card.period, card.day, teacher = rowCol_to_dayPeriodTeacher(self, row, column)


# Беремо зі списку й вилучаємо взятий елемент
def list_to_card(self, row):
    if row > self.ui.listView.model().rowCount() - 1:
        return None
    else:
        klAll = QtWidgets.QTableWidgetItem(self.ui.listView.model().item(row).text())
        klAll = klAll.text()
        klas, id_card = klAll.split("&")
        klas = klas.rstrip()
        id_card = id_card.rstrip()
        card = id_to_card(self.roz, id_card)
        self.roz.model.removeRow(self.ui.listView.selectedIndexes()[0].row())
        r = self.ui.listView.model().rowCount() - 1
        self.roz.lv_index = r

        return klas, card


# Записуємо до списку
def card_to_list(self, card):
    if card != None:
        id_card = card.id
        klas = ""
        for cl in card.lesson.classInThisLesson:
            klas += cl.short + " "
        klas = klas.strip()
        if klas != "":
            # Додати, якщо такого немає
            self.roz.model.appendRow(QStandardItem(klas + "                        &" + id_card))
            # Тут встановимо виділення в listView на останній елемент
            r = self.ui.listView.model().rowCount() - 1
            self.roz.lv_index = r
            ix = self.ui.listView.model().index(r, 0)
            self.ui.listView.selectionModel().setCurrentIndex(ix, QItemSelectionModel.ClearAndSelect)
        mySetCursor(self, klas)
    else:
        mySetCursor(self, "")


def cell_clicked(self):
    row = self.ui.tableWidget.currentRow()
    column = self.ui.tableWidget.currentColumn()
    klas, card = cell_to_card(self, row, column)

    if self.mode == "edit":
        list_row = -1
        klas0, card0 = None, None
        if self.ui.listView.model().rowCount() > 0:  # Беремо зі списку
            if self.roz.lv_index > -1:
                list_row = self.ui.listView.selectedIndexes()[0].row()
                klas0, card0 = list_to_card(self, list_row)

        # Беремо вміст комірок з таблиць


        klas, card = cell_to_card(self, row, column)



        # Вилучаємо з таблиць цю картку
        card_remove(self, card)

        # Записуємо до комірок таблиць
        if card0 != None:
            f = False
            for t in card0.lesson.teacherInThisLesson:
                if t.id == "*" + str(row + 1):
                    f = True
                    break
            if f:
                #       якщо урок учителя не відсутнього, то лише в його рядок
                card_to_cell(self, card0, row, column)

                #   шукаємо інших вчителів цієї картки та додаємо їх також
                for t in card0.lesson.teacherInThisLesson:
                   r = int(t.id[1:]) - 1  # номер рядка вчителя
                   if r == row:
                       continue
                   item = self.ui.tableWidget2.item(r, column)
                   if item != None:
                       klas_d, card_d = cell_to_card(self, r, column)
                       card_to_list(self, card_d)
                   card_to_cell(self, card0, r, column)
             #       вилучаємо до списку картки вчителів, до яких ставимо урок

            else:
                #       якщо урок відсутнього, то можна до іншого

                # -----
                #      Якщо це урок відсутнього вчителя, то вилучаємо його з картки

                # card0.lesson.teacherInThisLesson.remove(t)

                # -----

                #  Якщо поставити не вдалося, повертаємо картку назад до списку
                card_to_list(self, card0)

        # Записуємо до списку
        card_to_list(self, card)



    else:
        r, g, b = 255, 255, 255
        if card != None:
            ls = ""
            for s in card.lesson.subjInThisLesson:
                ls = ls + s.short
            cs = ""
            for c in card.lesson.classInThisLesson:
                cs += c.short
            self.ui.label.setText(ls)
            self.ui.tableWidget.setToolTip(card_to_tip(card))
            self.ui.pushButton_4.setText(cs)
            if card != None:
                s = card.lesson.teacherInThisLesson[0].color
            else:
                s = "#FFFFFF"
            r, g, b = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
        else:
            self.ui.pushButton_4.setText("")
            self.ui.label.setText("")
            self.ui.label.setToolTip("")
            self.ui.tableWidget.setToolTip("")
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(" + str(r) + "," + str(g) + "," + str(b) + ")")


def _cell_clicked(self):
    roz = self.roz
    row = self.ui.tableWidget.currentRow()
    column = self.ui.tableWidget.currentColumn()

    if self.mode == "edit":
        # Записуємо значення комірки до тимчасової змінної
        tmp = self.ui.tableWidget.item(row, column)
        tmp2 = self.ui.tableWidget2.item(row, column)
        if tmp == None:
            tmp = ""
            tmp2 = ""
        else:
            tmp = tmp.text()
            tmp2 = tmp2.text()
            #   Вилучаємо ім'я вчителя з картки
            c = id_to_card(self.roz, tmp2)
            if c != None:
                c.period, c.day, teacher = rowCol_to_dayPeriodTeacher(roz, row, column)
                # вилучатимемо вчителя лише коли він у відсутніх
                for i, t in enumerate(c.lesson.teacherInThisLesson):
                    if t.id == teacher.id:
                        c.lesson.teacherInThisLesson.remove(t)

        mySetCursor(self, tmp)

        # Записуємо до комірки значення зі списку

        self.ui.pushButton_4.setText(tmp)
        kl = ["", ""]
        kli = ["", ""]
        if roz.lv_index > -1:
            klAll = QtWidgets.QTableWidgetItem(self.ui.listView.model().item(self.roz.lv_index).text())
            klAll = klAll.text()
            kl = klAll.split("&")
            kl[0] = kl[0].rstrip()
            kl[1] = kl[1].rstrip()

            kli[0] = QtWidgets.QTableWidgetItem(kl[0])
            kli[1] = QtWidgets.QTableWidgetItem(kl[1])
        else:
            kli[0] = QtWidgets.QTableWidgetItem("")
            kli[1] = QtWidgets.QTableWidgetItem("")

        # Тут перевіримо, чи можна ставити. Якщо інший вчитель, то тільки урок відсутнього вчителя
        c = id_to_card(self.roz, kl[1])
        # визначаємо вчителя відсутнього з вибраному в списку
        teach = self.ui.listWidget.item(self.ui.listWidget.currentRow()).text()

        self.ui.tableWidget.setItem(row, column, kli[0])

        if c != None:
            if len(c.lesson.teacherInThisLesson) > 0:
                s = c.lesson.teacherInThisLesson[0].color
            else:
                s = "#FFFFFF"
            r, g, b = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
            self.ui.tableWidget.item(row, column).setBackground(QtGui.QColor(r, g, b))
            # Шукаємо за  id картку уроку та змінюємо в ній day, period
            c.period, c.day, teacher = rowCol_to_dayPeriodTeacher(roz, row, column)
            f = 0
            for t in c.lesson.teacherInThisLesson:
                if t == teacher:
                    f = 1
                    break
            if f == 0:
                c.lesson.teacherInThisLesson.append(teacher)
            self.ui.tableWidget.setToolTip(card_to_tip(c))
        self.ui.tableWidget2.setItem(row, column, kli[1])
        #           проходимо по стовпчику і вилучаємо картки з даним класом до списку
        #   тут не класи треба, а вчителів звільнять теж
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
                        roz.model.appendRow(QStandardItem(kl[0] + "                        &" + k_l))
                        k_l = QtWidgets.QTableWidgetItem("")
                        self.ui.tableWidget.setItem(r, column, k_l)

                        self.ui.tableWidget2.setItem(r, column, k_l)
            #    тепер перевіримо вчителів, що йдуть в парі

        # Вилучаємо зі списку зчитане значення
        roz.model.removeRow(self.roz.lv_index)

        # #           проходимо по стовпчику і вилучаємо картки з даною групою/класом до списку
        # if self.ui.tableWidget2.item(row, column) != None:
        #     s1 = self.ui.tableWidget2.item(row, column).text().strip()
        # else:
        #     s1 = ""
        # gr0 = cardId_to_groupId(roz, s1)
        # for r in range(0, len(roz.teachers) - 1):
        #     if r == row:
        #         continue
        #     if self.ui.tableWidget2.item(r, column) != None:
        #         s1 = self.ui.tableWidget2.item(r, column).text()
        #         # Шукаємо картку
        #         gr = cardId_to_groupId(roz, sl)
        #         if equGrups(gr0, gr):
        #             pass
        #
        #
        #
        #
        #
        #         # roz.model.appendRow(QStandardItem(kl[0] + "                        &" + k_l))
        #         # k_l = QtWidgets.QTableWidgetItem("")
        #         # self.ui.tableWidget.setItem(r, column, k_l)
        #         #
        #         # self.ui.tableWidget2.setItem(r, column, k_l)
        #
        # # Вилучаємо зі списку зчитане значення
        # roz.model.removeRow(self.roz.lv_index)

        if self.roz.lv_index > roz.model.rowCount() - 1:
            self.roz.lv_index = roz.model.rowCount() - 1
        if self.roz.lv_index > -1:
            tmp2 = self.ui.listView.model().item(self.roz.lv_index).text()
            if tmp2.index("&") > -1:
                x, y = tmp2.split("&")
            else:
                x = tmp2
                y = ""
            x = x.rstrip()
            self.ui.pushButton_4.setText(x)
        else:
            y = tmp2
        # Записуємо до списку значення, яке на початку було в комірці
        if tmp != "":
            roz.model.appendRow(QStandardItem(tmp + "                        &" + y))
            self.roz.lv_index = (roz.model.rowCount()) - 1
        # mySetCursor(self, tmp)
        if roz.model.rowCount() > 0:
            mySetCursor(self, tmp)

            # QApplication.setOverrideCursor(Qt.DragMoveCursor)

        else:
            pass
            # QApplication.setOverrideCursor(Qt.ArrowCursor)
            # QApplication.restoreOverrideCursor()

    else:
        print("Row %d and Column %d was clicked" % (row, column))
        r, g, b = 255, 255, 255
        item = self.ui.tableWidget2.item(row, column)

        if item != None:
            crd = id_to_card(roz, item.text())
            ls = ""
            for s in crd.lesson.subjInThisLesson:
                ls = ls + s.name
            self.ui.label.setText(ls)

            # day, period, teachId = rowCol_to_dayPeriod(roz, row, column)

            # c = roz.dopTable.get(dayPeriodTeach_to_addr(roz, day, period, teachId))

            self.ui.tableWidget.setToolTip(card_to_tip(crd))

            # timer.start(1000)

            # print (c.lessonid)
            self.ui.pushButton_4.setText(item.text())
            s = crd.lesson.teacherInThisLesson[0].color
            r, g, b = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
        else:
            self.ui.pushButton_4.setText("")
            self.ui.label.setText("")
            self.ui.label.setToolTip("")
            self.ui.tableWidget.setToolTip("")

        self.ui.pushButton_4.setStyleSheet("background-color: rgb(" + str(r) + "," + str(g) + "," + str(b) + ")")

        # self.ui.tableWidget.mouseReleaseEvent = self.myMouseReleaseEvent
        # self.ui.tableWidget.mousePressEvent = self.mousePressEvent

        # self.ui.tableWidget.dragEnterEvent = self.dragEnterEvent
        # self.ui.tableWidget.dropEvent = self.myDropEvent
        # self.ui.tableWidget.startDrag = self.myStartDrag

        # self.ui.tableWidget.setMouseTracking(True)
        # self.ui.tableWidget.installEventFilter(self)
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
    # self.ui.listWidget.addItem (item)
    # self.ui.listWidget.addItem (item)
    # self.ui.listWidget.addItem (item)
    # self.ui.listWidget.addItem (item)
    # self.ui.listWidget.addItem (item)
    # ui.show()
