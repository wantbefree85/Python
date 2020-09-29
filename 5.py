receipt = int(input("Введите количество выручки: "))
costs = int(input("Введите количество издержек: "))
if(receipt > costs):
    profitability = (receipt / costs) * 100
    print("Фирма работает в прибыль. Её рентабельность составляет: " + str(int(profitability)) + " %")
    persons = int(input("Введите количество сотрудников фирмы: "))
    print("прибыль фирмы в расчете на одного сотрудника составляет: " + str(round(((receipt - costs) / persons), 2)))
elif(receipt < costs):
    print("Фирма работает в убыток")
else:
    print("Фирма вышла в ноль")