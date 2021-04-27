import random


def number_correct(chosen_number, random_number):
    if chosen_number < random_number:
        print('Tu número es más grande.')
    else:
        print('Tú número es mas pequeño')


def run():
    random_number = random.randint(1, 100)
    chosen_number = int(input('Enter a number 1-100: '))
    while random_number != chosen_number:
        number_correct(chosen_number, random_number)
        chosen_number = int(input('Elige otro número: '))

    print('¡Felicidades! Encontraste el numero. 🥸 👍🏼')


if __name__ == '__main__':
    run()
