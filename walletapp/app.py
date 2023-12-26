from datetime import datetime

class Account:
    def __init__(self, account_name, opening_balance):
        self.__account_name = account_name
        self.__balance = opening_balance
        self.__created_date = datetime.now()
        self.__activated = True

    def display(self):
        print(self.__account_name + ' has an account balance: ' + str(self.__balance))

    def balanceInquiry(self):
        return self.__balance


class CreditCard(Account):
    def __init__(self, credit, account_name, opening_balance):
        self.__credit_limit = credit
        self.__due_date = None
        self.__extended_limit = 0
        self.__extended_until_date = None
        super().__init__(account_name, opening_balance)

    def display(self):
        #print('Hello World2')
        super().display()
        print('credit limit: ' + str(self.__credit_limit))
        #print(super().__account_name + ' has an account balance: ' + str(super().__balance))

    def display_extended(self):
        print('This is for extended account')


def run():
    bank_account01 = Account('Mr.A', 15000.00)
    bank_account01.display()

    cc_account01 = CreditCard(20000,'Mr.B',0)
    cc_account01.display()

    #Polymorph #1

    print ('A' + 'B' + 'C')
    print (1 + 2 + 3)

    v1 = 1
    v2 = '2'
    v3 = 3

    #print (v1 + int(v2) + v3)

    s1 = 'Hello Universe'
    s2 = [1,2,3,'aaa',5,8,9]

    print(len(s1))
    print(len(s2))

class A:
    def __init__(self,name,last_name):
        self.__name = name
        self.__last_name = last_name

    def display(self):
        print(self.__name + ' ' + self.__last_name)


class B:
    def __init__(self, name, credit):
        self.__name = name
        self.__credit = credit

    def display(self):
        print(self.__name + ' ' + str(self.__credit))


def run2():
    bank_account01 = Account('Mr.A', 15000.00)

    cc_account01 = CreditCard(20000,'Mr.B',0)

    list1 = [bank_account01, cc_account01]
    for i in list1:
        i.display()

    list2 = [A('Mr.C','Henman'), B('Mr.M',2000)]
    for j in list2:
        j.display()

def my_sum(args):
    # input can be string, list of int, or dictionary of int
    # Polymorphism #2 (data type)
    sum = 0
    if type(args) == str:
        numbers = args.split()
        for n in numbers:
            sum += int(n)

    if type(args) == list:
        for n in args:
            sum += n

    if type(args) == dict:
        vals = args.values()
        for n in vals:
            sum += n

    return sum


def run3():
    print(my_sum('10 20 30'))
    print(my_sum([10, 20, 31]))
    num = {
        '#1': 10,
        '#2': 20,
        '#3': 32
    }
    print(my_sum(num))


def display_name(firstname, lastname = '', title = ''):
    # this method can have one, two and three arguments !!
    # Polymorphism #3 (default argument)
    if title == '':
        title = 'Khun'

    if lastname == '':
        return title + ' ' + firstname + '\n'
    else:
        return title + ' ' + firstname + ' ' + lastname + '\n'

def run4():
    print(display_name('Albedo'))
    print(display_name('Eula', 'Lawrence'))
    print(display_name('Prinzessin', 'der Verurteilung!', 'mein Fräuleins'))