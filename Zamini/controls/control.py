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
        if card.lesson.teacherInThisLesson[0] != None:  #перестрахуємося на випадок, якщо немає в картці вчителів
            s = card.lesson.teacherInThisLesson[0].color    #змінюємо колір комірки на колір вчителя
            r, g, b = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
            self.ui.tableWidget.item(row, column).setBackground(QtGui.QColor(r, g, b))

        card.day, card.period, teacher = rowCol_to_dayPeriodTeacher(self, row, column)
        # self.ui.label_2.setText("День-"+str(card.day)+" Урок-"+str(card.period))

# Беремо зі списку й вилучаємо взятий елемент
def list_to_card(self, row):
    if row > self.ui.listView.model().rowCount() - 1:
        return None
    else:
        klAll = QtWidgets.QTableWidgetItem(self.ui.listView.model().item(row).text())
        klAll = klAll.text()
        klas, teacher, id_card = klAll.split("_")
        klas = klas.rstrip()
        teacher = teacher.rstrip()
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
        teacher = ""
        for cl in card.lesson.classInThisLesson:
            klas += cl.short + " "
        for tc in card.lesson.teacherInThisLesson:
            teacher += tc.short + " "
        klas = klas.strip()
        teacher = teacher.strip()

        if klas != "":
            # Додати, якщо такого немає
            self.roz.model.appendRow(QStandardItem(klas + " _"  +teacher+ " _" + id_card))
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
                #   не працює із зведеними класами
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
                # проходимо по таблиці, і знайшовщи відповідний клас, переносимо його урок до списку
                # з таблиці ж прибираємо
                for t in self.roz.teachers:
                    r = int(t.id[1:]) - 1  # номер рядка вчителя
                    if r == row:
                        continue
                    item = self.ui.tableWidget2.item(r, column)
                    if item != None:
                        klas_e, card_e = cell_to_card(self, r, column)
                        if klas_e.strip() == klas0.strip():
                            card_to_list(self, card_e)
                            card_remove(self, card_e)

            else:
                #       якщо урок відсутнього, то можна до іншого

                # -----
                #      Якщо це урок відсутнього вчителя, то вилучаємо його з картки

                # card0.lesson.teacherInThisLesson.remove(t)

                # -----

                #  Якщо поставити не вдалося, повертаємо картку назад до списку
                pass
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
            print("day="+str(card.day)+" period="+str(card.period))
        else:
            self.ui.pushButton_4.setText("")
            self.ui.label.setText("")
            self.ui.label.setToolTip("")
            self.ui.tableWidget.setToolTip("")
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(" + str(r) + "," + str(g) + "," + str(b) + ")")


