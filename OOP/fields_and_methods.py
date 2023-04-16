class Person:
    def __init__(self, first_name, last_name, age, sex):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.sex = sex

    def say_hi_n_times(self, n):
        for i in range(n):
            print(f"Hi! I'm {self.name} {self.surname}. What's your name?")

    def change_name(self, new_first_name, new_last_name):
        self.name = new_first_name
        self.surname = new_last_name

person1 = Person("Adam", "Feliniak", "32", "m")
person2 = Person("Anna", "Kowalska", "30", "k")

person1.say_hi_n_times(3)
person1.change_name("Max", "Payne")
person1.say_hi_n_times(1)