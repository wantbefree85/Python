a = int(input("Сколько спортсмен пробежал километров в первый день: "))
b = int(input("Введите день, чтобы узнать прогресс спортсмена: "))
count=1
while(True):
    if(b==int(a)):
        break
#    print(str(count) + "-й день: " + str(round(a,2)))
    a += ((a/100)*10)
    count += 1
print("На " + str(count) + "-й день спортсмен достиг результата - не менее " + str(int(a)) + " км.")