def input_numbers(var_1, var_2):
    if(var_2==0):
        print("Деление на ноль не выполнимо!")
        return 0
    print(var_1 / var_2)

var_1 = int(input("Введите первое число: "))
var_2 = int(input("Введите второе число: "))
input_numbers(var_1, var_2)