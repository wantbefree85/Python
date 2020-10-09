count = 0
salary = 0
with open('task_3.txt') as file_3:
    print('Зарплата сторудников меньше 20000:')
    for string in file_3:
        count += 1
        array = string.split()
        salary += int(array[1])
        if int(array[1]) < 20000:
            print(array[0])
    print(f'Средняя зарплата сотрудников: {str(salary/count)}')