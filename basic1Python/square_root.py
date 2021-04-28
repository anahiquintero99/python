import math


def run():
    number = int(input('Ingresa número: '))
    square_number = int(math.sqrt(number))

    if number % square_number == 0:
        print(f'{number} = {square_number} Es raiz cuadrada exacta.')
    else:
        print('La raiz cuadrada no es exacta.')


if __name__ == '__main__':
    run()
