class Student:
    ids = set()
    def __init__(self, first_name, last_name, age, sex, idnum):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.idnum = None
        self.set_id(idnum)


    def introduce(self):
        print(f"Ja {self.first_name} {self.last_name} jestem studentem")

    def get_id(self):
        return self.idnum

    def set_id(self, new_idnum):
        if new_idnum not in Student.ids:
            Student.ids.add(new_idnum)
            self.idnum = new_idnum
        else:
            while new_idnum in Student.ids:
                new_idnum *= 10
            Student.ids.add(new_idnum)
            self.idnum = new_idnum
            #raise Exception("Student o podanym id już istnieje!")

    @classmethod
    def list_student_ids(cls):
        return sorted(cls.ids)



student1 = Student("Jan", "Nowak", 20, "m", 12345)
student2 = Student("Alicja", "Wkrainieczarów", 21, "k", 54321)
student3 = Student("Gill", "Bates", 22, "m", 12345)
student4 = Student("Jan", "Nowak", 20, "m", 12345)
print(student1.get_id())
print(student3.get_id())
print(student4.get_id())
print(student4.list_student_ids())





