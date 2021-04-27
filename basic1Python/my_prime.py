def number_prime(number):
    if number % 1 == 0:
        for i in range(2, number):
            value = int(number % i)
            if value == 0:
                return True
                break
            else:
                continue


def run():
    number = int(input('Enter number: '))
    if number == 1:
        print('No es primo')
    elif number_prime(number) == True:
        print('No es primo')
    else:
        print('Es primo')


if __name__ == '__main__':
    run()
