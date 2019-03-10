from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,\
                            QWidget, qApp

""""
def getForCard(day,period,weeks):
    
    clas_s=[]
    teach_s=[]
    subj_s=[]
    classr_s=[]
    group_s=[]
    for c in cards:
        if c.day == day:
            if c.period==period:
                if (c.weeks==weeks):
                    clas_s =clas_s + (c.classInThisLesson)
                    teach_s = teach_s + (c.teacherInThisLesson)
                    subj_s = subj_s + (c.subjInThisLesson)
                    classr_s = classr_s + (c.classroomsInThisLesson)
                    group_s = group_s + (c.groupInThisLesson)
                    
    return clas_s, teach_s, subj_s, classr_s,group_s
"""
def getForCard(roz, day, period, teach, weeks):

    for c in roz.cards:
        if c.day == day:
            if c.period==period:
                tFlag = False
                for t in c.teacherInThisLesson:
                    if t.id == teach:
                        tFlag = True
                if ((c.weeks == weeks) or (c.weeks == "1")) and (tFlag):
                    return c
    return None

def id_to_card(roz, id):
    for c in roz.cards:
        if id == c.id:
            return c
    return None

def rowCol_to_dayPeriod(roz, row, col):
    day = col // roz.periods_count
    period = col % roz.periods_count + 1
    teachId = "*" + str(row+1)
    return day, period, teachId



def rowCol_to_addr(roz, row, col):
    day = col // roz.periods_count
    period = col % roz.periods_count + 1
    teachId = "*" + str(row + 1)
    return dayPeriodTeach_to_addr(roz, day, period, teachId)

def dayPeriodTeach_to_addr(roz, day, period, teachId):   #teachId Приклад "*1"
    row = int(teachId[1:]) - 1
    col = len(roz.periods) * int(day) + int(period) - 1
    return "R"+str(row)+"C"+str(col)



def addr_to_dayPeriodTeach(roz,adr):
    n = adr.find("C")
    teachId = "*"+adr[1:n]
    col = int(adr[n + 1:])
    day = col // roz.periods_count
    period = col % roz.periods_count + 1
    return day, period, teachId

def addr_to_card(roz, adr):
    print(adr)
    return len(roz.cards)

def fillTable(self, ui, radioButton, roz):
    # Заповнення таблиці
    ui.tableWidget.setColumnCount(0)
    ui.tableWidget.setRowCount(0)
    ui.tableWidget2.setColumnCount(0)
    ui.tableWidget2.setRowCount(0)
    roz.dopTable = {}
    ui.tableWidget.setColumnCount(len(roz.days) * len(roz.periods))
    ui.tableWidget.setRowCount(len(roz.teachers))
    ui.tableWidget2.setColumnCount(len(roz.days) * len(roz.periods))
    ui.tableWidget2.setRowCount(len(roz.teachers))

    for col in range(0, len(roz.days) * len(roz.periods) + 1):
        ui.tableWidget.setColumnWidth(col, 40)
        ui.tableWidget2.setColumnWidth(col, 40)
    labelHor = []
    for d in roz.days:
        for p in roz.periods:
            if p.period == "1":
                tt = d.short
            else:
                tt = ""
            labelHor.append(tt + "\n" + p.period)

            ui.tableWidget.setHorizontalHeaderLabels(labelHor)
            ui.tableWidget2.setHorizontalHeaderLabels(labelHor)
    labelVert = []
    for t in roz.teachers:
        labelVert.append(t.short)
        ui.tableWidget.setVerticalHeaderLabels(labelVert)
        ui.tableWidget2.setVerticalHeaderLabels(labelVert)
    for c in roz.cards:
        col = len(roz.periods) * int(c.day) + int(c.period) - 1
        w = c.weeks
        if (radioButton.isChecked()) and (w == "01"):
            continue
        if (radioButton.isChecked() == False) and (w == "10"):
            continue
        for t in c.lesson.teacherInThisLesson:
            row = int(t.id[1:]) - 1
            ss = ""
            for cc in c.lesson.classInThisLesson:
                ss += cc.short
            kl = QtWidgets.QTableWidgetItem(ss)
            ui.tableWidget.setItem(row, col, kl)
            ui.tableWidget2.setItem(row, col, QtWidgets.QTableWidgetItem(c.id))
            s = t.color
            r, g, b = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
            ui.tableWidget.item(row, col).setBackground(QtGui.QColor(r, g, b))
            #roz.dopTable[row][col] = c
            #roz.dopTable["R"+str(row)+"C"+str(col)] = c



