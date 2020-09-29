num = int(input('Input number'))
a = (num % 10)
while(num):
    b = (num//10) % 10
    if(a<b):
        a=b
    num = num // 10
print("Самое большое число в указанной последовательности: " + str(a))