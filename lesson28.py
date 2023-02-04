class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_info(self):
        print("Студент", self.name, "учится на", self.course, "курсе")


student1 = Student("Шмуговец", 6)
student2 = Student("Пригодич", 3)
student3 = Student("Карпач", 2)
student4 = Student("Волк", 4)
student5 = Student("Воробьёв", 1)
student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()
student5.display_info()
