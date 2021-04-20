# Square root of twho

def run():
    LIMIT = 1000
    NUMBER = 2

    account = 0
    square = NUMBER ** account
    while square < LIMIT:
        print(f'\n{NUMBER} ** {account} = {square}')
        account = account + 1
        square = NUMBER ** account


if __name__ == '__main__':
    run()
