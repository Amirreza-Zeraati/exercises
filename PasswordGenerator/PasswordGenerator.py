from random import shuffle, choice
from string import ascii_letters, digits


characters = list(ascii_letters + digits + "!@#$%^&*()")


def PasswordGenerator():
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
    print(password)
    details = input('Enter Specific Details About Your Password : ')
    SavePassword('passwords.txt', details, password)
    opt = input('Generate Another Password ? [y/n]')
    if opt.lower() == 'n':
        break
