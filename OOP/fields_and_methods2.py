class Car:
    how_many_cars_so_far = 0
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.velocity = 0
        Car.how_many_cars_so_far += 1

    def speed_up(self):
        self.velocity += 1

    def slow_down(self):
        self.velocity -= 1
        if self.velocity < 0:
            self.velocity = 0
    @classmethod
    def get_name(cls):
        if cls.how_many_cars_so_far == 0:
            return "samochodów"
        elif cls.how_many_cars_so_far == 1:
            return "samochód"
        elif cls.how_many_cars_so_far < 5:
            return "samochody"
        else:
            return "samochodów"

print(Car.how_many_cars_so_far)

my_car = Car("Daewoo", "Lanos", "zielony")
my_car.color = "czerwony"
print(my_car.color)
print(Car.how_many_cars_so_far)
my_car.speed_up()
print(my_car.velocity)
my_car.slow_down()
my_car.slow_down()
my_car.slow_down()
print(my_car.velocity)
renault = Car('Renault', 'Ancara', 'czerwony')
fiat = Car('Fiat', '126p', 'silver')
fiat2 = Car('Fiat', '126p', 'silver')
fiat3 = Car('Fiat', '126p', 'silver')



print(f"Jak na razie wyprodukowano {Car.how_many_cars_so_far} {Car.get_name()}.")
