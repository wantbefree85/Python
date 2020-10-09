dict_er = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task_4.txt') as file_4:
    new_file_4 = open('new_task_4.txt', 'w')
    for line in file_4:
        string = line.split(' - ')
        print(f'{dict_er[string[0]]} - {string[1]}', file=new_file_4)
    new_file_4.close()