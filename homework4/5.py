from functools import reduce
def multiply(num1, num2):
    return num1 * num2
print(reduce(multiply, [num for num in range(100 , 1001, 2)]))