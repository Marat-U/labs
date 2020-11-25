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
        self.collection.append(item)

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
        return self.name + " " + str(self.class_list)

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


pupil1 = Pupil("Petya Ivanov")
pupil2 = Pupil("Anton Sidorov")
pupil3 = Pupil("Sveta Petrova")
pupil4 = Pupil("Nina Svetlova")
class1 = Class("10", [pupil1, pupil2])
class2 = Class("11", [pupil3, pupil4])

lists = ListIterator()
lists.add(class1)
lists.add(class2)

while lists.has_next():
        print(str(lists.current()))
        lists.next()

teacher1 = Teacher("Antonina Lvovna", "math")
teacher2 = Teacher("Taras Petrovich", "lit")

teacher1.add_score_pupil(5, pupil1)
teacher1.add_score_pupil(3, pupil1)
teacher1.add_score_pupil(3, pupil2)

print(pupil1.data, pupil2.data)
