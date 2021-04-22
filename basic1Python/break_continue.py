
def run():
    #    for number in range(100):
    #       if number % 2 == 0:
    #           continue
    #        print(number)

    #    for i in range(10):
    #        print(i)
    #        if i == 5:
    #            break

    texto = input('Ingresa texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()
