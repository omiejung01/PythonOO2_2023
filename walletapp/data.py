class Account:
    def __init__(self,account_name,opening_balance):
        self.account_name = account_name
        self.balance = opening_balance
    #Constructor

    def display(self):
        # Balance Inquiry
        return self.account_name + ' ' + f"{self.balance:,.2f}"

    def setAccountName(self, new_name):
        self.account_name = new_name

class Character:
    def __init__(self, character_name, vision, weapon_type):
        self.__character_name = character_name
        self.__vision = vision
        self.__weapon = None
        self.__weapon_type = weapon_type


    def display(self):
        #self.__weapon.display()
        weapon_name = ''
        if self.__weapon is not None:
            weapon_name = self.__weapon.getWeaponName()

        print(self.__character_name + ' ' + self.__vision + ' ' + weapon_name)

    def setCharacterName(self, new_name):
        self.__character_name = new_name

    def getCharacterName(self):
        return self.__character_name

    def getWeaponType(self):
        return self.__weapon_type

    def setWeapon(self, weapon):
        if weapon.getWeaponType() == self.__weapon_type:
            self.__weapon = weapon
            print('Equipped!!!')
        else:
            print(self.__character_name + ' cannot use ' + weapon.getWeaponName())



class Weapon:
    def __init__(self,weapon_name, weapon_type):
        self.__weapon_name = weapon_name
        self.__weapon_type = weapon_type
        self.__level = 1

    def display(self):
        print(self.__weapon_name + ' ' + self.__weapon_type +' ' + str(self.__level))

    def getWeaponType(self):
        return self.__weapon_type

    def getWeaponName(self):
        return self.__weapon_name


def run():
    dull_blade = Weapon('Dull Blade','Sword')
    #dull_blade.display()

    #raiden_character = Character('Raiden Shogun', 'Electro', dull_blade)
    #raiden_character.display()  # Display “Raiden Shogun Electro” on the screen

    #raiden_character.__character_name = 'Yae Miko'
    # This is not working because encapsulation (Information Hiding)
    #raiden_character.setCharacterName('Yae Miko')

    raiden_character = Character('Raiden Shogun', 'Electro', 'Polearm')

    amos_bow = Weapon('Amos Bow','Bow')

    raiden_character.setWeapon(amos_bow)
    raiden_character.display()

    engulfing_lightning = Weapon('Engulfing Lightning','Polearm')
    raiden_character.setWeapon(engulfing_lightning)
    raiden_character.display()

    #raiden_character.display()
    #print(raiden_character.getCharacterName())

    # raiden_character.character_name = 'Yae Miko'
    # raiden_character.display()

    # List
    my_list = ['Dehya', 'Candace']
    print (len(my_list))
    my_list.append('Cyno')
    print(len(my_list))

    # 1st Element
    print(my_list[0])

    # Last element
    print(my_list[len(my_list)-1])


    navia_character = {
        "Name": "Navia",
        "weapon_type": "Claymore",
        "vision": 'Geo'
    }

    print(navia_character['Name'])
    print(navia_character['weapon_type'])







