class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        pass
    def m_road(self):
        return (self._length * self._width * 25 * 5) / 1000


calc = Road(20, 5000)
print(f"{int(calc.m_road())} т")