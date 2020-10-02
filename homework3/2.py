def description_user(name, surname, birthday, city, email, phone_numb):
    print("Пользователь: Имя - {0}, Фамилия - {1}, День Рождения - {2}, Город-{3}, email - {4}, телефон - {5}"
        .format(name, surname, birthday, city, email, phone_numb))
description_user(name = 'Андрей', surname='Ковалев', birthday='26.07.1985', city='Санкт_Петербург',
                 email='want_be_free@yahoo.com', phone_numb='+79522690986')