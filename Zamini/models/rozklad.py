import controls.modelsbuild as mb

class Rozklad(object):
    def __init__(self, fileName):
        days, periods, teachers, classes, subjects, classrooms, groups, lessons, cards = mb.Build(fileName)
        self.days = days
        self.periods = periods
        self.teachers = teachers
        self.classes = classes
        self.subjects = subjects
        self.classrooms = classrooms
        self.groups = groups
        self.lessons = lessons
        self.cards = cards
        self.dopTable ={}
        self.periods_count=0
        oldCard = None
        """
        rowCount = len(teachers)
        colCount = (len(days)+1)* len(periods)
        for r in range(0, rowCount):
            d = []
            for c in range(0, colCount):
                d.append(0)
            self.dopTable.append(d)
        """


        #clas_s, teach_s, subj_s, classr_s, group_s = r.getForCard(cards, "0", "7", "1")

