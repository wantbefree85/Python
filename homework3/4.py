def my_func(x, y):
    print("Метод '**': " + str(x ** y))
    multiply = x
    for i in range(1, abs(y)):
        x = x * multiply
    if(y<0):
        print("Метод цикла: " + str(1/x))
    else:
        print("Метод цикла: " + str(x))

my_func(2,-2)