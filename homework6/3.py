class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        # self.get_full_name()
        # self.get_total_income()

    def get_full_name(self):
        print(f"{self.surname} {self.name}")

    def get_total_income(self):
        print(f"Total salary is {self._income['wage'] + self._income['bonus']}")


incomes = {'wage': 5000, 'bonus': 2000}
work_1 = Position('Andrey', 'Kovalev', 'chief engineer', incomes)
work_1.get_full_name()
work_1.get_total_income()