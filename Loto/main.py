from random import randint, shuffle
from temp import ChekVal  # ИМПОРТ КЛАССА ChekVal

class LotoCard():
    def __init__(self):
        self.line = '------------------------------'
        self.list_str = []
        self.list_1 = self.shuff_numbers()
        self.list_2 = self.shuff_numbers()
        self.list_3 = self.shuff_numbers()

    def shuff_numbers(self):
        listing = []
        i = 1
        listing.append(randint(0, 91))
        self.list_str.append(listing[0])
        while i != 5:
            val = randint(0, 91)
            if val in listing or val in self.list_str:
                continue
            else:
                listing.append(val)
                self.list_str.append(val)
                i += 1
        for j in range(5, 9):
            listing.append('_')
            shuffle(listing)
        return listing

    def convert_list(self):
        return f"{self.line}\n{'  '.join(str(el) for el in self.list_1)}\n" \
               f"{ '  '.join(str(el) for el in self.list_2)}\n" \
               f"{'  '.join(str(el) for el in self.list_3)}\n{self.line}"

class LotoGame():
    def __init__(self, human, computer):
        self.u_card = human
        self.pc_card = computer
        print(f"Ваша Карта\n{self.u_card.convert_list()}")
        print(f"Карта Компьютера\n{self.pc_card.convert_list()}")

    def start(self):
        flag = True
        val_store = []
        self.cp_count= 15
        self.user_count = 15
        while flag:
            val = randint(0, 91)
            if val in val_store:
                continue
            else:
                val_store.append(val)
            print(f'\nБоченок под номером - {val}')
            flag = ChekVal.check_numb(self, self.cp_count, self.user_count, numb=val)
            if self.cp_count == 0:
                print(f"Увы, вы проиграли, компьютер вычеркнул все боченки из карточки\n{self.pc_card.convert_list()}")
                break
            elif self.user_count == 0:
                print(f"Поздравляю, вы выиграли, все цифры вычеркнуты\n{self.u_card.convert_list()}")
                break

user = LotoCard()
pc = LotoCard()
game = LotoGame(human=user, computer=pc)
game.start()