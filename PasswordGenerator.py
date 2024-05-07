import random

char_map = {
    'a': ['a', '@'],
    'o': ['o', '0'],
    'i': ['i', '1', '!', '|'],
    'u': ['u', 'n'],
    'e': ['e', '3'],
    's': ['s', '$', '5'],
    't': ['t', '+'],
    'z': ['z', '2'],
    'c': ['c', '(', '{', '<', '['],
    'd': ['d', ')', ']', '>', '}'],
}

def list_to_string(list_of_characters: list) -> str:
    '''
    Function to transform character list to string
    :param list_of_characters: A list containing characters
    :return: Returns a string
    '''
    string = ''
    for char in list_of_characters:
        string += str(char)

    return string

def generate_random_password(length, list_of_chars):
    generated_characters = []
    for i in range(length):
        random_index = random.randint(1, length)
        generated_characters.append(list_of_chars[random_index])

    random.shuffle(generated_characters)

    return list_to_string(generated_characters)

def generate_password(word):
    password = ''
    for char in word:
        char = char.lower()
        replacement = char_map.get(char, [char])
        ch = random.choice(replacement)
        if ch.isalpha():
            ch = random.choice([ch.lower(), ch.upper()])
        password += ch
    return password


if __name__ == '__main__':
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    special = '@#$%^&*()-+!'
    characters = alpha + num + special

    # Dynamic length of password
    length_of_password = random.randint(8, 13)

    password = ''

    user_input = input(
        'Enter any, word or sentence or even a length of password below: \n')

    if user_input.isdigit():
        length_of_user_input = int(user_input)
        if length_of_user_input > 50:
            print("Length of password can't be greater than 50.")
            password = generate_password(length_of_password, characters)
        else:
            print(f'Generating password of length {length_of_user_input}')
            password = generate_random_password(length_of_user_input, characters)
    else:
        if user_input.__len__() == 0:
            password = generate_random_password(length_of_password, characters)
        else:
            print(f'Using {user_input} as basis for password.')
            password = generate_password(word=user_input)

    if password is not None:
        print(f'New Password: {password}')
