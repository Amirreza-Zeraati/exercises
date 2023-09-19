from random import shuffle, choice
from string import ascii_letters, digits, punctuation


'''
    we can use punctuation; but we dont need that much special characters
    punctuation :  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    if you like it, do this:
    characters = list(ascii_letters + digits + punctuation)
'''
characters = list(ascii_letters + digits + "[]{}()*&^%$#@!~")


def PasswordGenerator():
    '''
        at first we have this
        ['a', 'b', 'c', 'd', ... , '&', '*', '(', ')']
        then we shuffle it to pick randomly
        ['v', 'o', '0', '*', ... , 'O', '$', 'V', 'u', '8']
        after pick enough, shuffle it again or more shure
        length = 8
        ['e', 'r', '6', 'n', 'j', '*', 'q', 'S']
        by using .join() method we finally got password
        --  er6nj*qS  --
    '''
    length = int(input("Enter Password Length : "))
    shuffle(characters)
    password = [choice(characters) for i in range(length)]
    shuffle(password)
    return "".join(password)


def SavePassword(path, detail, password):
    with open(path, 'a') as file:
        file.write(f'{password} : {detail}\n')
    file.close()


while True:
    password = PasswordGenerator()
    print("Your Password is : ", password)
    details = input('Enter Specific Details About Your Password : ')
    SavePassword('passwords.txt', details, password)
    opt = input('Generate Another Password ? [y/n]')
    if opt.lower() == 'n':
        break
