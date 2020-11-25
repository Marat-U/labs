class ListIterator():

    def __init__(self, collection = []):
        self.collection = collection
        self.cursor = 0

    def current(self):
        if self.cursor < len(self.collection):
            return self.collection[self.cursor]

    def next(self):
        if len(self.collection) >= self.cursor + 1:
            self.cursor += 1

    def has_next(self):
        has = len(self.collection) >= self.cursor + 1
        if not has: self.cursor = 0
        return has

    def add(self, item):
        self.collection += [item]

class Pupil:
    def __init__(self, name):
        self.name = name
        self.data = {"math" : [], "prog" : [], "lit" : []}

    def add_score(self, subj, score):
        self.data[subj].append(score)

    def __repr__(self):
        return self.name + " " + str(self.data)

class Class:
    def __init__(self, name, class_list = []):
        self.name = name
        self.class_list = class_list

    def __repr__(self):
        return "Номер класса: " + self.name + "; Список учеников: " + str(self.class_list)

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
                if pupil.name == pupil_work:
                    pupil.add_score(self.subj, score_dict[pupil_work])

    def create_class_list(self, class_list):
        self.teacher_class_list += (class_list)

    def __repr__(self):
        return self.name

class Administrator:
    def __init__(self, classes_num):
        self.classes_num = classes_num

    def pupil_eval(self, pupil):
        mean = {}
        for subj in pupil.data:
            scores = pupil.data[subj]
            if scores:
                avg = sum(scores) / len(scores)
                mean[subj] = avg
        return mean

    def class_eval(self, class_num):
        mean = {}
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
        return self.teacher_mean_grade



pupil1 = Pupil("Petya Ivanov")
pupil2 = Pupil("Anton Sidorov")
pupil3 = Pupil("Sveta Petrova")
pupil4 = Pupil("Nina Svetlova")
class1 = Class("10", [pupil1, pupil2])
class2 = Class("11", [pupil3, pupil4])

lists = ListIterator()
lists.add(class1)
lists.add(class2)

print("Заполнили классный журнал:")
while lists.has_next():
        print("\t" + str(lists.current()))
        lists.next()

teacher1 = Teacher("Antonina Lvovna", "math")
teacher2 = Teacher("Taras Petrovich", "lit")

teacher1.add_score_pupil(5, pupil1)
teacher1.add_score_pupil(4, pupil2)
teacher1.add_score_pupil(4, pupil3)
teacher2.add_score_pupil(3, pupil2)
teacher2.add_score_pupil(3, pupil3)
teacher2.add_score_pupil(5, pupil4)

teacher1.add_score_class_dict(class1, {"Petya Ivanov" : 5, "Sveta Petrova" : 2})
teacher1.add_score_class_dict(class2, {"Sveta Petrova" : 5, "Nina Svetlova" : 3})

print("\nПоставили ученикам оценки:")
while lists.has_next():
        print("\t" + str(lists.current()))
        lists.next()


administrator1 = Administrator(["10", "11"])
teacher1.create_class_list([class1, class2])
teacher2.create_class_list([class1, class2])
teacher2_eval = float(administrator1.teacher_eval(teacher2))

print("\nОцениваем работу учителя:")
while lists.has_next():
        print("\t" + str(lists.current()))
        lists.next()
print("Средняя оценка ", teacher2, ": " , "{:.2f}".format(teacher2_eval))
