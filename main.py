# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import bcrypt

#pip install bcrypt

def my_salt():
    return ('$2b$12$tUimG74HOCBiAA7sm3QX9e').encode('utf-8')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_password='abcdefg'

    bytePwd = input_password.encode('utf-8')
    hash = bcrypt.hashpw(bytePwd, my_salt())

    new_password = hash.decode('utf-8')

    print(new_password)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
