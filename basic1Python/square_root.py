import math


def run():
    number = int(input('Ingresa número: '))
    square_number = int(math.sqrt(number))

    if number % square_number == 0:
        print(f'Raiz cuadrada de {number} es {square_number} es exacta.')
    else:
        print(f'{number} No tiene raiz cuadrada exacta.')


if __name__ == '__main__':
    run()
