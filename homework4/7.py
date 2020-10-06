from math import factorial

fact = lambda n: [factorial(i) for i in range(1, n+1)]  # Анонимная функция вычисления факториала
def generator():
    for el in fact(n):
        yield el

n = int(input("Введите число:"))
for i in generator():
    print(i)