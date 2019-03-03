class Lesson(object):

    def __init__(self,id,subjectid,classids,groupids,studentids,teacherids,classroomids,periodspercard,periodsperweek,weeks):
        self.id=id
        self.subjectid=subjectid
        self.classids=classids
        self.groupids=groupids
        self.studentids=studentids
        self.teacherids=teacherids
        self.classroomids=classroomids
        self.periodspercard=periodspercard
        self.periodsperweek=periodsperweek
        self.weeks=weeks

        self.teacherInThisLesson = []
        self.classInThisLesson = []
        self.subjInThisLesson = []
        self.groupInThisLesson = []
        self.classroomsInThisLesson = []

    def setClassroom(self,classrooms):
        ss = self.classroomids.split(",")
        for ts in ss:
            for t in classrooms:
                if t.id==ts:
                    self.classroomsInThisLesson.append(t)

    def setGroup(self,groups):
        ss = self.groupids.split(",")
        for ts in ss:
            for t in groups:
                if t.id==ts:
                    self.groupInThisLesson.append(t)


    def setTeacher(self,teachers):
        ss = self.teacherids.split(",")
        for ts in ss:
            for t in teachers:
                if t.id==ts:
                    self.teacherInThisLesson.append(t)

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
