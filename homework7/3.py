class Cell:
    def __init__(self, cell_number):
        self.num = cell_number

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if (self.num - other.num) > 0:
            return self.num - other.num
        else:
            return "Разность ячеек клеток меньше нуля"

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return int(self.num / other.num)

    def make_order(self, nir):  # СМОГ НАПИСАТЬ, ТОЛЬКО ПОСЛЕ РАЗБОРА ДОМАШНЕГО ЗАДАНИЯ
        return '\n'.join(['*' * nir for _ in range(self.num // nir)]) + '\n' + '*' * (self.num % nir)


cell_1 = Cell(30)
cell_2 = Cell(20)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(10))