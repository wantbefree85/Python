with open('task_1.py', 'w') as file_1:
    while True:
        string = input('Input line: ')
        if not string:
            break
        file_1.write(string + '\n')