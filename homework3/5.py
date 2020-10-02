def sum_numbers(digits, symb):
    list_number = digits.split()
    for i in range(0, len(list_number)):
        if list_number[i] == symb:  # ПРОВЕРКА НА НАЛИЧИЕ СПЕЦ СИМВОЛА
            print("\nВВЕДЕН СПЕЦИАЛЬНЫЙ СИМВОЛ: " + symb)
            return sum(list(map(int, list_number[:i]))), 1
    return sum(list(map(int, list_number))), 0

""" НАЧАЛО ПРОГРАММЫ """
total = 0  # ПЕРЕМЕННАЯ, ДЛЯ ХРАНЕНИЯ ОБЩЕЙ СУММЫ
symbol = input("Введите специальный символ: ")
while(True):
    numb = input("\nВведите строку чисел, разделенных пробелом: ")
    num, flag = sum_numbers(numb, symbol)  # Вызов функции суммы введенных чисел и проверки по вводу СПЕЦ символа
    if flag == 1:  # если был введен СПЕЦ символ, то подсчитываем сумму и выходим из проги
        total += num
        break
    total += num
    print("Сумма чисел равна: " + str(total))
print("Общая сумма всех введенных чисел составляет: " + str(total))