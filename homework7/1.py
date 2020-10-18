class Matrix:
    def __init__(self, list_m):
        self.list_m = list_m
        self.i = -1

    def __str__(self):
        # return str(self.list_m) - ЭТО ТО, ЧТО БЫЛО ДО ТОГО, КАК Я ПОСМОТРЕЛ РАЗБОР ДОМАШНЕГО ЗАДАНИЯ
        return '\n'.join([' '.join([str(el) for el in line]) for line in self.list_m])

    def __add__(self, other):
        if len(self.list_m) != len(other.list_m):
            return "Invalid input data!"
        else:
            for j in range(0, len(other.list_m)):
                l_m1 = self.list_m[j]
                l_m2 = other.list_m[j]
                for k in range(0, len(other.list_m)):
                    l_m1[k] = l_m1[k] + l_m2[k]
                self.list_m[j] = l_m1
            return self.list_m


list_m1 = [[1, 2, 3],
           [2, 4, 5],
           [6, 2, 8]]
list_m2 = [[4, 2, 1],
           [5, 2, 6],
           [6, 5, 8]]
mx1 = Matrix(list_m1)
mx2 = Matrix(list_m2)
print(mx1)
print(mx2)
print(mx1 + mx2)