from random import randint


class Unit:
    def __init__(self,  hp: int, dmg: int, dodge: int, name: str):
        self.__hp: int = hp
        self.__dmg: int = dmg
        self.__dodge: int = dodge
        self.__name: str = name

    def attack(self, enemy):
        enemy.hp = enemy.hp - self.__dmg

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, new_hp: int):
        self.__hp = new_hp

    @property
    def dmg(self):
        return self.__dmg

    @property
    def dodge(self):
        return self.__dodge

    @property
    def name(self):
        return self.__name

Swordsman = Unit(15, 5, 60, "Swordsman")
Archer = Unit(12, 4, 40, "Archer")
Mage = Unit(8, 10, 30, "Mage")

def main_make_teams():
    """ Makes 2 teams, 3 members in each"""
    first = []
    second = []
    i = 0
    while i < 3:
        number1team = randint(1, 3)
        if number1team == 1:
            first.append(Swordsman)
        elif number1team == 2:
            first.append(Archer)
        elif number1team == 3:
            first.append(Mage)

        number2team = randint(1, 3)
        if number2team == 1:
            second.append(Swordsman)
        elif number2team == 2:
            second.append(Archer)
        elif number2team == 3:
            second.append(Mage)
        i += 1
    return first, second


try:
    teams = main_make_teams()
    team1 = teams[0]
    team2 = teams[1]
except Exception as e:
    print("Error is =>", e)


def start_game():
    count_hp_1team = team1[0].hp + team1[1].hp + team1[2].hp
    count_hp_2team = team2[0].hp + team2[1].hp + team2[2].hp
    print(f"\nПочатковий рахунок: {count_hp_1team}:{count_hp_2team}")
    exit = False
    while not exit:
        try: 
            # Визначаємо хто з команди атакує і кого атакує:           
            ataking_numb = randint(1, 3)
            ataked_numb = randint(1, 3)

            # 1-ша команда атакує            
            input("Натисніть Enter щоб атакувати!\n")
            print("1-ша команда атакує")
            if ataking_numb == 1:
                ataking = team1[0]
            elif ataking_numb == 2:
                ataking = team1[1]
            elif ataking_numb == 3:
                ataking = team1[2]

            if ataked_numb == 1:
                ataked = team2[0]
            elif ataked_numb == 2:
                ataked = team2[1]
            elif ataked_numb == 3:
                ataked = team2[2]

            print(f"{ataking.name} з 1-ї команди нападає на {ataked.name} з 2 команди ")
            chanse_to_live = randint(1, 100)
            if chanse_to_live > ataked.dodge:
                print("Атака успішна")
                ataking.attack(ataked)
                print("{} втратив {} життів. ".format(ataked.name, ataking.dmg))
                count_hp_2team = count_hp_2team - ataking.dmg
                print("Рахунок: {}:{}\n".format(count_hp_1team, count_hp_2team))
            else:
                print("Атака не вдалась...\n")

            # 2-га команда атакує
            input("Натисніть Enter для контратаки!\n")
            print("2-га команда атакує")
            if ataking_numb == 1:
                ataking = team2[0]
            elif ataking_numb == 2:
                ataking = team2[1]
            elif ataking_numb == 3:
                ataking = team2[2]

            if ataked_numb == 1:
                ataked = team1[0]
            elif ataked_numb == 2:
                ataked = team1[1]
            elif ataked_numb == 3:
                ataked = team1[2]

            print(f"{ataking.name} з 2-ї команди нападає на {ataked.name} з 1 команди ")
            chanse_to_live = randint(1, 100)
            if chanse_to_live > ataked.dodge:
                print("Атака успішна")
                ataking.attack(ataked)
                print("{} втратив {} життів. ".format(ataked.name, ataking.dmg))
                count_hp_1team = count_hp_1team - ataking.dmg
                print("Рахунок: {}:{}\n".format(count_hp_1team, count_hp_2team))
            else:
                print("Атака не вдалась...\n")

            if count_hp_1team <= 0 or count_hp_2team <= 0:
                exit = True
                print("Гру закінчено!")                
                if count_hp_1team > count_hp_2team:
                    print("Виграла 1 команда!!! \nУ них залишилось {} хітпоінтів.\n".format(count_hp_1team))
                elif count_hp_1team < count_hp_2team:
                    print("Виграла 2 команда!!! \nУ них залишилось {} хітпоінтів.\n".format(count_hp_2team))
                else:
                    print("Нічия, перемогла дружба!!!\n")
            else:
                exit = False        

        except Exception as error:
            print("Error in while => ", error)

    return count_hp_1team, count_hp_2team


try:
    start_game()
except Exception as e:
    print("Error start_game =>", e)
