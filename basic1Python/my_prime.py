def number_prime(number):
    if number % 1 == 0:
        for i in range(2, number):
            if number % i == 0:
                return True
                break
            else:
                return False


def run():
    number = int(input('Enter number: '))
    if number_prime(number) == True:
        print('No es primo')
    else:
        print('Es primo')


if __name__ == '__main__':
    run()
