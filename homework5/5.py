sum = 0
file_5 = open('task_5.txt', 'w')
print(input('Введите последовательно числа через пробел: '), file=file_5)
file_5.close()
with open('task_5.txt', 'r') as file_5:
    line = file_5.readline()
    list = line.split(' ')
    for i in range(0, len(list)):
        sum += int(list[i])
    print(f"Сумма введеных чисел: {sum}")