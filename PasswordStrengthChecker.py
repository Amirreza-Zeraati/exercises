import string


def check_password_strength():
    password = input('Enter The Password : ')
    strength = 0
    details = ''
    lower_count = upper_count = num_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        # elif char in string.punctuation:
        #     special_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
    if len(list(password)) >= 8:
        strength += 1

    if strength == 1:
        details = 'This is a very BAD password, Change it as soon as possible'
    elif strength == 2:
        details = 'This is a weak password, You should consider using a tougher password'
    elif strength == 3:
        details = 'Your password is okay, but it can be improved'
    elif strength == 4:
        details = 'Your password is hard to guess, But you could make it even more secure'
    elif strength == 5:
        details = 'Your password is really strong'

    print('Your password have : ')
    print(f'> {len(list(password)} characters -has to be 8 at least-')
    print(f'> {lower_count} lowercase letters')
    print(f'> {upper_count} uppercase letters')
    print(f'> {num_count} digits')
    print(f'> {special_count} special characters')
    print(f'Password Score: {(strength / 5) * 100}%')
    print(f'More details : {details}')


while True:
    check_password_strength()
    opt = input('Check Another Password ? [Y/N] : ')
    if opt.lower() == 'n':
        break
