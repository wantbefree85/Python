from sys import argv
func_name, working_hours, pay_per_hour, extra_payment = argv
def salary_counting(x,y,z):
    salary = (int(x) * int(y)) + int(z)
    print(f"Выработка в часах: {x}\nСтавка в час: {y}\nПремия: {z}\nЗарплата: {salary}")

salary_counting(working_hours, pay_per_hour, extra_payment)