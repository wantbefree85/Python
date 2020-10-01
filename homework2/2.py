list=[]
while(True):
    list.append(input("Введите элемент списка: "))
    print("Если хотите завершить ввод, наберите 'quit' и нажмите enter")
    if(list[-1]=='quit'.lower()):
        break
print(list)
for var in range(1, len(list), 2):
    list_el=list[var-1]
    list[var-1]=list[var]
    list[var]=list_el
print(list)
