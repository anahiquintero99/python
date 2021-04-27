import random


def generator_password():
    capital_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = capital_letter + lowercase + symbols + numbers

    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)

    password = "".join(password)
    return password


def run():
    password = generator_password()
    print(f'Tú nueva contraseña es: {password}')


if __name__ == '__main__':
    run()
