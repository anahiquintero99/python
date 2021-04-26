def number_prime(number):
    contador = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return False


def run():
    number = int(input('Enter number: '))
    if number_prime(number):
        print('It is prime')
    else:
        print('It is not prime')


if __name__ == '__main__':
    run()
