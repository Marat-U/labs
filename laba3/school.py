class Pupil:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number
        self.data = {"math" : [], "prog" : [], "lit" : []}

    def add_score(self, subj, score):
        self.data[subj].append(score)

    #def __str__(self):
    #    return self.name

    def __repr__(self):
        return self.name + " " + self.surname + " " + self.number + " " + str(self.data)

class Class:
    def __init__(self, name):
        self.name = name
        self.class_list = []

    def fill_class_list(self, person):
        self.class_list.append(person)
        person.number = self.name

    def __repr__(self):
        return self.name

class Teacher:
    def __init__(self, name, subj):
        self.name = name
        self.subj = subj
        self.teacher_class_list = []

    def add_score_pupil(self, score, pupil):
        pupil.add_score(self.subj, score)

    def add_score_class_dict(self, class_num, score_dict):
        for pupil_work in score_dict:
            for pupil in class_num.class_list:
                if pupil.surname == pupil_work:
                    pupil.add_score(self.subj, score_dict[pupil_work])

    def create_class_list(self, class_list):
        self.teacher_class_list += (class_list)


class Administrator:
    def __init__(self, name, classes_num):
        self.name = name
        self.classes_num = classes_num

    def pupil_eval(self, pupil):
        mean = {}
        for subj in pupil.data:
            scores = pupil.data[subj]
            if scores:
                avg = sum(scores) / len(scores)
                mean[subj] = avg
        return mean

    def class_eval(self, class_num): #функция итерирующая список классов и считающая средние оценки учеников
        mean = {}
        self.grades = []
        self.all = []
        self.final = []
        for pupil in class_num.class_list:
            pupil_avg = self.pupil_eval(pupil)
            for subj in pupil_avg:
                mean[subj] = mean.get(subj, []) + [pupil_avg[subj]]
        for subj in mean:
            mean[subj] = sum(mean[subj]) / len(mean[subj])

        return mean


    def teacher_eval(self, teacher):
        self.teacher_eval_list = []
        self.final_list = []
        for class_num in teacher.teacher_class_list:
            for pupil in class_num.class_list:
                if teacher.subj in pupil.data:
                    self.teacher_eval_list += pupil.data[teacher.subj]
        for item2 in self.teacher_eval_list:
            self.final_list.append(item2)
        self.teacher_mean_grade = sum(self.final_list) / len(self.final_list)

pupil1 = Pupil("Petya", "Ivanov", "9")
pupil2 = Pupil("Sveta", "Petrova", "10")

pupil1.add_score("math", 5)
pupil1.add_score("prog", 4)
pupil1.add_score("prog", 5)
pupil1.add_score("lit", 5)
print(pupil1.data)
print(pupil1)


pupil2.add_score("prog", 5)


class1 = Class("10")
class2 = Class("11")

class1.fill_class_list(pupil1)
class1.fill_class_list(pupil2)
class2.fill_class_list(pupil2)

print(class1.class_list)

teacher1 = Teacher("Galina", "lit")
teacher1.add_score_pupil(2, pupil1)
print(pupil1)

teacher1.add_score_class_dict(class1, {"Petrova" : 5, "Ivanov" : 1})
print(class1.class_list)

administrator1 = Administrator("Anton Petrovich", ["9", "10"])
print(administrator1.class_eval(class1))
'''
print(administrator1.grades)
print(administrator1.all)
print(administrator1.final)
print(round(administrator1.pupil_mean_grade, 2))
'''
teacher2 = Teacher("Alexander", "math")
teacher1.create_class_list([class1, class2])
teacher2.create_class_list([class1, class2])
teacher2.add_score_class_dict(class1, {"Petrova": 3, "Ivanov": 4})
print(teacher1.name, teacher1.teacher_class_list)
print(teacher2.name, teacher2.teacher_class_list)

administrator1.teacher_eval(teacher2)
print(class1.class_list)
print(class2.class_list)
print(administrator1.teacher_mean_grade)
