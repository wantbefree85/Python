class ChekVal():

    @staticmethod
    def check_numb(self, cp_count, user_count, numb):
        if numb in self.pc_card.list_1:
            self.pc_card.list_1[self.pc_card.list_1.index(numb)] = 'X'
            print(f'Компьютер зачеркнул число {numb}\n{self.pc_card.convert_list()}')
            self.cp_count -= 1
            return True
        elif numb in self.pc_card.list_2:
            self.pc_card.list_2[self.pc_card.list_2.index(numb)] = 'X'
            print(f'Компьютер зачеркнул число {numb}\n{self.pc_card.convert_list()}')
            self.cp_count -= 1
            return True
        elif numb in self.pc_card.list_3:
            self.pc_card.list_3[self.pc_card.list_3.index(numb)] = 'X'
            print(f'Компьютер зачеркнул число {numb}\n{self.pc_card.convert_list()}')
            self.cp_count -= 1
            return True
        else:
            choose = input(f'{self.u_card.convert_list()}\nВы желаете ЗАЧЕРКНУТЬ или ПРОДОЛЖИТЬ "З/П" ? ')
            choose = choose.lower()

            if numb in self.u_card.list_1 and choose == 'з':
                self.u_card.list_1[self.u_card.list_1.index(numb)] = 'X'
                print(f"Молодец, число {numb} было вычеркнуто из вашей карты\n{self.u_card.convert_list()}")
                self.user_count -= 1
                return True
            elif numb in self.u_card.list_2 and choose == 'з':
                self.u_card.list_2[self.u_card.list_2.index(numb)] = 'X'
                print(f"Молодец, число {numb} было вычеркнуто из вашей карты\n{self.u_card.convert_list()}")
                self.user_count -= 1
                return True
            elif numb in self.u_card.list_3 and choose == 'з':
                self.u_card.list_3[self.u_card.list_3.index(numb)] = 'X'
                print(f"Молодец, число {numb} было вычеркнуто из вашей карты\n{self.u_card.convert_list()}")
                self.user_count -= 1
                return True
            elif numb not in self.u_card.list_1 and choose == 'з':
                print(f"Вы проиграли, так как зачеркнули число {numb} которого НЕТ в вашей крточке")
                return False
            elif numb not in self.u_card.list_2 and choose == 'з':
                print(f"Вы проиграли, так как зачеркнули число {numb} которого НЕТ в вашей крточке")
                return False
            elif numb not in self.u_card.list_3 and choose == 'з':
                print(f"Вы проиграли, так как зачеркнули число {numb} которого НЕТ в вашей крточке")
                return False
            elif (numb in self.u_card.list_1 or numb in self.u_card.list_2 or numb in self.u_card.list_3) \
                    and (choose == 'п'):
                print(f"Вы проиграли, так как не увидели число {numb} в своей карточке")
                return False
            elif numb not in self.u_card.list_1 and choose == 'п':
                print(f"Молодец, числа {numb} нет в вашей карте")
                return True
            elif numb not in self.u_card.list_2 and choose == 'п':
                print(f"Молодец, числа {numb} нет в вашей карте")
                return True
            elif numb not in self.u_card.list_3 and choose == 'п':
                print(f"Молодец, числа {numb} нет в вашей карте")
                return True

