class Teamlead:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def set_task_person(self, task, area, person):
        person.set_task(task, area)

    def set_task_department(self, task, area):
        for department in self.departments:
            if area == department.depart_description:
                department.set_task(task)

class Department:
    depart_description = ""
    def __init__(self, persons):
        self.persons = persons

    def set_task(self, new_task): # ["create_calendar", 2]
        min_person_time = 9999999
        for i in range(len(self.persons)):
            person_time = 0
            for task in self.persons[i].tasks:
                person_time += task[1]
            if person_time < min_person_time:
                min_person_time = person_time
                min_person = self.persons[i]
        min_person.tasks.append(new_task)

    def __str__(self):
        s = self.depart_description + ':\n'
        for person in self.persons:
            s += '\t' + person.__str__() + '\n'
        return s

class Frontend(Department):
    def __init__(self, persons):
        super().__init__(persons)
        self.depart_description = "Frontend"
        for person in self.persons:
            person.profession = self.depart_description

    def set_task(self, new_task): # ["create_calendar", 2]
        super().set_task(new_task)

class Backend(Department):
    def __init__(self, persons):
        super().__init__(persons)
        self.depart_description = "Backend"
        for person in self.persons:
            person.profession = self.depart_description

    def set_task(self, new_task): # ["create_calendar", 2]
        super().set_task(new_task)

class Employee:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks # [["create_button", 3], ["create_window", 5]]
        self.profession = None

    def set_task(self, task, area):
        if self.profession == area:
            self.tasks.append(task)
        else:
            print("Cannot do the task")

    def finish_task(self):
        if len(self.tasks) > 0:
            self.tasks.pop(0)

    def __repr__(self):
        return self.name + " " + str(self.tasks)


employee1 = Employee("Oleg", [["create_button", 3], ["create_window", 10]])
employee2 = Employee("Grisha", [["create_menu", 5]])
employee3 = Employee("Steve", [["debug_database", 4]])

frontend_depart = Frontend([employee1, employee2])
backend_depart = Backend([employee3])
frontend_depart.set_task(["create_template", 4])
print(employee1.tasks)
print(employee2.tasks)
print(employee3.tasks)

employee1.finish_task()
print(employee1.tasks)
print(frontend_depart)

teamlead1 = Teamlead("Ivan", [frontend_depart, backend_depart])
#teamlead1.set_task_person(["create_logo", 2], "Frontend", employee1)
teamlead1.set_task_department(["create_logo", 2], "Frontend")

teamlead1.set_task_department(["add_receive_function", 4], "Backend")
teamlead1.set_task_person(["create_main_paige", 2], "Backend", employee1)

print(employee1.tasks)
print(frontend_depart)
print(backend_depart.persons)

employee1.finish_task()
employee1.finish_task()
