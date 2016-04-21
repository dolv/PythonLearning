class Student(object):
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.labGrades = []
        self.examGrade = 0
        for lab in range(config['lab_num']):
            self.labGrades.append(0)

    def make_lab(self, receivedGrade, labNumber=None):
        if labNumber is None:
            if any(grade == 0 for grade in self.labGrades):
                labNumber = self.labGrades.index(0)
        if labNumber < self.config['lab_num'] and labNumber >= 0:
            self.labGrades[labNumber] = min(receivedGrade, self.config['lab_max'])
            return self

    def make_exam(self, examGrade):
        self.examGrade = min(examGrade, self.config['exam_max'])
        return self

    def is_certified(self):
        earned = sum(self.labGrades) + self.examGrade
        total = len(self.labGrades) * self.config['lab_max'] + self.config['exam_max']
        return (earned, earned >= total * self.config['k'])

# conf = {
# 'exam_max': 30,
# 'lab_max': 7,
# 'lab_num': 10,
# 'k': 0.61,
# }
# oleg = Student('Oleg', conf)
# oleg.make_lab(1) \
# .make_lab(8,0) \
# .make_lab(1) \
# .make_lab(10,7) \
# .make_lab(4,1) \
# .make_lab(5) \
# .make_lab(6.5) \
# .make_exam(32)
# print oleg.is_certified() # (59.5, False)
# oleg.make_lab(7,1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
# print oleg.is_certified() # (62.5, True)

conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}
# o1 = Student('Oleg', conf1)
# print o1.is_certified()
# print
# o2 = Student('Oleg', conf1)
# o2.make_lab(60).make_lab(35.2)
# print o2.is_certified()
# print
o3 = Student('Oleg', conf1)
o3.make_lab(10).make_lab(10).make_exam(15)
print o3.is_certified()
o3.make_lab(20,1).make_lab(20,0)
print o3.is_certified()
o3.make_lab(50,2)
print o3.is_certified()
o3.make_lab(40,1)
print o3.is_certified()
print
# conf2 = {'exam_max': 52,'lab_max': 8,'lab_num': 6,'k': 0.5}
# o5 = Student('Oleg', conf2)
# o5.make_lab(40).make_lab(7,5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7,1)
# print o5.is_certified()
# o5.make_lab(7)
# print o5.is_certified()
# print
# conf3 = {'exam_max': 10,'lab_max': 1,'lab_num': 90,'k': 0.5,}
# o6 = Student('Oleg', conf3)
# for i in range(51): o6.make_lab(1)
# print o6.is_certified()