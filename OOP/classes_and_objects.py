class A:
    pass

object1 = A()
object2 = A()
print(id(object1))
print(id(object1))

class Person:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.surname = last_name
        self.age = age
        self.sex = sex

person1 = Person("Adam", "Feliniak", "32", "m")
person2 = Person("Anna", "Kowalska", "30", "k")

print(person1.age)

