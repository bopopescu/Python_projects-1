from random import randint
class Unit:
    def __init__(self,  hp:int, dmg:int, dodge:int):
        self.__hp:int = hp
        self.__dmg:int = dmg
        self.__dodge:int = dodge

@property
def hp(self):
    return self.__hp

@hp.setter
def hp(self, new_hp:int):
    self.__hp = new_hp

@property
def dmg(self):
    return self.__dmg

@dmg.setter
def dmg(self, new_dmg:int):
    self.__dmg = new_dmg

@property
def dodge(self):
    return self.__dodge

@dmg.setter
def dmg(self, new_dmg):
    self.__dmg = new_dmg

Swordsman = Unit(15, 5, 60)
Archer = Unit(12, 4, 40)
Mage = Unit(8, 10, 30)

def main_make_teams():
    """ Makes 2 teams, 3 members in each"""
    first = []
    second = []    
    i=0
    while i<3:
        number1team = randint(1,3)        
        if number1team == 1:
           first.append(Swordsman)
        elif number1team == 2:
           first.append(Archer)
        elif number1team == 3:
           first.append(Mage) 

        number2team = randint(1,3)
        if number2team == 1:
           second.append(Swordsman)
        elif number2team == 2:
           second.append(Archer)
        elif number2team == 3:
           second.append(Mage)        
        i += 1
    return first, second 
# exit = False
# while not exit:
    # print("To start game press Enter!")
try:
    teams = main_make_teams()
    team1 = teams[0] 
    team2 = teams[1]
    # print(team1)
    print(team1[0])
except Exception as e:
    print("Error is =>", e)

