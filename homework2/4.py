string = (input("Введите строку: "))
string = string.split()
print(string)
for var in range(0, len(string)):
    section = string[var]
    print(str(var + 1) + ": " + section[0:10])