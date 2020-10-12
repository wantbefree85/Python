class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("The car is moving now...")

    def stop(self):
        print("The car is stopped now...")

    def turn(self, direction):
        direction = direction.lower()
        if direction == 'left':
            print("The car is turned to the Left.")
        elif direction == 'right':
            print("The car is turned to the Left.")

    def show_speed(self, speed):
        print(f"The {self.name} car speed is {speed} MPH")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 60:
            print("WARNING, you've increase your speed limit!!! No more then 60 MPH")
        print(f"Current speed is {speed} MPH")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 40:
            print("WARNING, you've increase your speed limit!!! No more then 40 MPH")
        print(f"Current speed is {speed} MPH")


sport_c = SportCar(200, 'Yellow', 'Ferrari', False)
police_c = PoliceCar(150, 'Black&white', 'Ford', True)
town_c = TownCar(60, 'Grey', 'Buick', False)
work_c = WorkCar(40, '"Dirty"', 'GMC', False)

# Доступ к атрибутам и вывод результатов
print(f"1) {sport_c.name}, color - {sport_c.color}, max speed - {sport_c.speed} MPH, Police - {sport_c.is_police}")
print(f"2) {police_c.name}, color - {police_c.color}, max speed - {police_c.speed} MPH, Police - {police_c.is_police}")
print(f"3) {town_c.name}, color - {town_c.color}, max speed - {town_c.speed} MPH, Police - {town_c.is_police}")
print(f"4) {work_c.name}, color - {work_c.color}, max speed - {work_c.speed} MPH, Police - {work_c.is_police}")

# Вызов методов и их результат
print(sport_c.name), sport_c.go(), sport_c.turn('right')
print(police_c.name), police_c.stop(), print(police_c.is_police)
print(town_c.name), town_c.go(), town_c.show_speed(70)
print(work_c.name), work_c.go(), work_c.turn('left'), work_c.show_speed(10)
