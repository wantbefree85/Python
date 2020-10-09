count = 0
with open('task_2.txt') as file_2:
    for line in file_2:
        count += 1
        print(f'Количество строк в строке № {count}: {len(line.split())}')
    print(f'Всего строк: {count}')