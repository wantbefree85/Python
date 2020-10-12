class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title, name):
        super().__init__(title)
        self.name = name

    def draw(self):
        print(f'Программа {self.title}, инструмент: "{self.name}"')


class Pencil(Stationery):
    def __init__(self, title, name):
        super().__init__(title)
        self.name = name

    def draw(self):
        print(f'Программа {self.title}, инструмент: "{self.name}"')


class Handle(Stationery):
    def __init__(self, title, name):
        super().__init__(title)
        self.name = name

    def draw(self):
        print(f'Программа {self.title}, инструмент: "{self.name}"')

pen = Pen('Канцелярия', 'Ручка')
pen.draw()
pencil = Pencil('Канцелярия', 'Карандаш')
pencil.draw()
handle = Handle('Канцелярия', 'Маркер')
handle.draw()