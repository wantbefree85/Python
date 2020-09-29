numeric = int(input("Input number: "))
num = str(numeric)
string = str(num)
sum = numeric
while(numeric-1):
    string = string + num
    numeric -= 1
    sum = sum + int(string)
print(sum)
