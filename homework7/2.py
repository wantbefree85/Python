from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, val):
        self.value = val

    @abstractmethod
    def tot_consumption(self):
        pass

class Coat(Clothes):
    @property
    def tot_consumption(self):
        c_cons = self.value / 6.5 + 0.5
        return c_cons

class Suit(Clothes):
    @property
    def tot_consumption(self):
        s_cons = 2 * self.value + 0.3
        return s_cons


suit = Suit(int(input("Введите размер костюма H: ")))
coat = Coat(int(input("Введите рост V: ")))
print(f"Расход ткани на костюм составляет: {int(suit.tot_consumption)}")
print(f"Расход ткани на пальто составляет: {int(coat.tot_consumption)}")