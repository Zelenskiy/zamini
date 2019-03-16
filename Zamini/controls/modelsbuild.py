import controls.xml_parser as xp
import models.day as rd
import models.period as rp
import models.teachers as rt
import models.classes as rc
import models.subjects as rs
import models.classrooms as rcr
import models.groups as rg
import models.lessons as rl
import models.cards as rcrd
import copy



def Build(fileName):
    #Формуємо об'єкти розкладу'
    xml = xp.readXml(fileName)

    days = []
    periods = []
    teachers=[]
    classes=[]
    subjects=[]
    classrooms=[]
    groups=[]
    lessons=[]
    cards=[]

    for child in xml:
        if child.tag == "days":
            for d in child:
                d0 = rd.Day( d.get("name"), d.get("short"),d.get("day"))
                days.append(d0)
        elif child.tag == "periods":
            for d in child:
                d0 = rp.Period( d.get("period"), d.get("starttime"),d.get("endtime"))
                periods.append(d0)
        elif child.tag == "teachers":
            for d in child:
                d0 = rt.Teacher( d.get("id"), d.get("name"),d.get("short"),d.get("gender"),d.get("color"))
                teachers.append(d0)
        elif child.tag == "classes":
            for d in child:
                d0 = rc.Class( d.get("id"), d.get("name"),d.get("short"),d.get("classroomids"),d.get("teacherid"))
                classes.append(d0)
        elif child.tag == "subjects":
            for d in child:
                d0 = rs.Subject( d.get("id"), d.get("name"),d.get("short"))
                subjects.append(d0)
        elif child.tag == "classrooms":
            for d in child:
                d0 = rcr.Classroom( d.get("id"), d.get("name"),d.get("short"))
                classrooms.append(d0)
        elif child.tag == "groups":
            for d in child: #classid,name,entireclass,divisiontag,studentcount
                d0 = rg.Group( d.get("id"), d.get("name"),d.get("classid"),d.get("entireclass"),d.get("divisiontag"),d.get("studentcount"))
                groups.append(d0)
        elif child.tag == "lessons":
            for d in child: #id,subjectid,classids,groupids,studentids,teacherids,classroomids,periodspercard,periodsperweek,weeks
                d0 = rl.Lesson( d.get("id"), d.get("subjectid"),d.get("classids"),d.get("groupids"),d.get("studentids"),
                                d.get("teacherids"), d.get("classroomids"),d.get("periodspercard"),d.get("periodsperweek"),d.get("weeks") )
                d0.setTeacher(teachers)
                d0.setClass(classes)
                d0.setGroup(groups)
                d0.setClassroom(classrooms)
                d0.setSubjects(subjects)
                lessons.append(d0)



        elif child.tag == "cards":
            id = 0
            for d in child: #lessonid,day,period,classroomids
                id = id + 1
                d0 = rcrd.Card("*"+str(id), d.get("lessonid"), d.get("day"), d.get("period"), \
                                d.get("classroomids"))
                #d0.setFields(lessons,days,periods)

                # Визначаємо урок
                d0.lesson = None
                for ll in lessons:
                    if ll.id == d0.lessonid:
                        d0.lesson = copy.deepcopy(ll)
                        # d0.lesson = ll
                        break

                n = int(d0.lesson.periodspercard)
                if n == 1:
                    cards.append(d0)
                else:
                    cards.append(d0)
                    d1 = copy.deepcopy(d0)
                    # d1 = d0
                    id = id + 1
                    d1.id = "*"+str(id)
                    for less in range(1, n):
                        d1.period = str(int(d1.period) + 1)
                        cards.append(d1)
                        #

                #Якщо periodspercard="2" (спарений урок) додаємо дві картки


    # print ("============ ",len(cards))
    return days,periods,teachers,classes,subjects,classrooms,groups,lessons, cards
