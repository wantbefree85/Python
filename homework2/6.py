goods = []  # СПИСОК ТОВАРОВ
position = []  # ДИНАМИЧЕСКИЙ СПИСОК --> В ДАЛЬНЕЙШЕМ КОРТЕЖ из номера и словаря с товарами
item = {}  # СЛОВАРЬ С ТОВАРАМИ
analyze = {'Название': [], 'Цена': [], 'Количество': [], 'ед': []}  # СЛОВАРЬ С АНАЛИТИКОЙ
num = 1  # НУЛЕВАЯ ПОЗИЦИЯ КОРТЕЖА
while True:
    item['Название'] = input("Введите название товара: ")
    item['Цена'] = int(input("Введите цену на товар: "))
    item['Количество'] = int(input("Введите количество выбранного товара: "))
    item['ед'] = input("Введите единицы выбранного товара:")
    for key, val in item.items():
        analyze[key].append(val)
    it = dict.copy(item)  # создаем копию словаря
    position.append(num)
    position.append(it)
    goods.append(tuple(position))
    list(position)
    position.clear()
    num += 1
    print("Продолжить ввод данных? Да/Heт")
    if input().lower() == 'нет':
        break

for var in range(0, len(goods)):
    print(goods[var])
for key, val in analyze.items():
    print(key + ": " + str(val))