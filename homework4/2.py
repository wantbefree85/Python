from random import randrange, randint

origin_list = [randrange(100) for num in range(randint(5,20))]
print(f"Исходный список: {origin_list}")
new_list = [origin_list[i] for i in range(1, len(origin_list)) if origin_list[i-1] < origin_list[i]]
print(f"Новый список: {new_list}")