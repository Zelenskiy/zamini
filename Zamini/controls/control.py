from PyQt5 import QtCore, QtWidgets, QtGui

from PyQt5.QtGui import QStandardItem, QImage, QBitmap, QPainter, QFont, QPen, QBrush, QColor
from PyQt5.QtWidgets import QApplication
from controls.funcRozklad import rowCol_to_dayPeriod, dayPeriodTeach_to_addr, \
    rowCol_to_addr, addr_to_dayPeriodTeach, getForCard, id_to_card
from PyQt5.QtCore import Qt, QTimer, QRect, QPoint
from PyQt5.QtGui import QPixmap

from controls.funcRozklad import rowCol_to_dayPeriodTeacher


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
        self.setCursor(QtGui.QCursor(bmp, 0, 0))
    else:
        QApplication.setOverrideCursor(Qt.ArrowCursor)


def cell_clicked(self, roz, row, column):
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
                for i, t in enumerate(c.lesson.teacherInThisLesson):
                   if t.id == teacher.id:
                       c.lesson.teacherInThisLesson.remove(t)

        mySetCursor(self, tmp)


        # Записуємо до комірки значення зі списку
        # TODO

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
        self.ui.tableWidget.setItem(row, column, kli[0])
        c = id_to_card(self.roz, kl[1])
        if c != None:
            if len(c.lesson.teacherInThisLesson)>0:
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
                        roz.model.appendRow(QStandardItem(kl[0] + "                        &" + k_l))
                        k_l = QtWidgets.QTableWidgetItem("")
                        self.ui.tableWidget.setItem(r, column, k_l)

                        self.ui.tableWidget2.setItem(r, column, k_l)

        # Вилучаємо зі списку зчитане значення
        roz.model.removeRow(self.roz.lv_index)

        if self.roz.lv_index > roz.model.rowCount() - 1:
            self.roz.lv_index = roz.model.rowCount() - 1
        if self.roz.lv_index > -1:
            tmp2 = self.ui.listView.model().item(self.roz.lv_index).text()
            if tmp2.index("&") > -1:
                x, y = tmp2.split("&")
            else:
                x = tmp2
            x = x.rstrip()
            self.ui.pushButton_4.setText(x)
        # Записуємо до списку значення, яке на початку було в комірці
        if tmp != "":
            roz.model.appendRow(QStandardItem(tmp + "                        &" + tmp2))
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
            cl = id_to_card(roz, item.text())
            ls = ""
            for s in cl.lesson.subjInThisLesson:
                ls = ls + s.name
            self.ui.label.setText(ls)

            day, period, teachId = rowCol_to_dayPeriod(roz, row, column)

            # c = roz.dopTable.get(dayPeriodTeach_to_addr(roz, day, period, teachId))
            t_s = ""
            for t in cl.lesson.teacherInThisLesson:
                t_s += t.short + " "
            c_s = ""
            for c in cl.lesson.classInThisLesson:
                c_s += c.short + " "

            self.ui.tableWidget.setToolTip(cl.lesson.subjInThisLesson[0].short + "\n" + \
                                           c_s + "\n" + \
                                           t_s);

            # timer.start(1000)

            # print (c.lessonid)
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
