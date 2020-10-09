import json
my_list = []
diction = {}
profit_dict = {}
loos_dict = {}
looses = {'Looses': {}}
aver_prof = 0
with open('task_7.txt', encoding='utf-8') as file_7:
    for line in file_7:
        string = line.split()
        if int(string[2]) >= int(string[-1]):
            diction[string[0]] = int(string[2]) - int(string[-1])
            aver_prof += diction[string[0]]
        else:
            loos_dict[string[0]] = int(string[2]) - int(string[-1])
            looses['Looses'] = loos_dict
    my_list.append(diction)
    profit_dict['average_profit'] = aver_prof
    my_list.append(profit_dict)
    if looses['Looses']:
        my_list.append(looses)
    print(my_list)
with open('task_7.json', 'w', encoding='utf-8') as json_7:
    json.dump(my_list, json_7)