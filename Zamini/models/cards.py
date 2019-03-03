class Card(object):
    def __init__(self,lessonid,day,period,classroomids):
        self.lessonid=lessonid
        self.day=day
        self.period=period
        self.classroomids=classroomids

        self.teacherInThisLesson = []
        self.classInThisLesson = []
        self.subjInThisLesson = []
        self.groupInThisLesson = []
        self.classroomsInThisLesson = []


    def setFields(self,lessons,days,periods):
        for l in lessons:
            if l.id==self.lessonid:
                for t in l.teacherInThisLesson:
                    self.teacherInThisLesson.append(t)
                for cr in l.classroomsInThisLesson:
                    self.classroomsInThisLesson.append(cr)
                for g in l.groupInThisLesson:
                    self.groupInThisLesson.append(g)
                for s in l.subjInThisLesson:
                    self.subjInThisLesson.append(s)
                for c in l.classInThisLesson:
                    self.classInThisLesson.append(c)
                self.weeks = l.weeks
            for d in days:
                if d.day==self.day:
                    self.dayShort = d.short
                    self.dayName = d.name
                    break
            for p in periods:
                if p.period==self.period:
                    self.periodShort = p.period
                    break

"""
    def setClassroom(self,classrooms):
        ss = self.classroomids.split(",")
        for ts in ss:
            for t in classrooms:
                if t.id==ts:
                    self.classroomsInThisLesson.append(t)

    def setGroup(self,lessons):
        ss = self.groupids.split(",")
        for ts in ss:
            for t in groups:
                if t.id==ts:
                    self.groupInThisLesson.append(t)




    def setClass(self,classes):
        ss = self.classids.split(",")
        for cs in ss:
            for c in classes:
                if c.id==cs:
                    self.classInThisLesson.append(c)


    def setSubjects(self,subjects):
        for s in subjects:
            if s.id == self.subjectid:
                self.subjInThisLesson.append(s)
"""
