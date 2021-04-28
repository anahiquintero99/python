# function to add data to list
def info():
    name = input('What is your name?: ')
    years = int(input('How old are you?: '))
    people = []
    people.append(name)
    people.append(years)
    return people

# fuction to compare one age with another age


def run():
    first = info()
    second = info()

    if second[1] > first[1]:
        print(f'{second[0]} {second[1]} es mayor que {first[0]}{first[1]}')
    elif second[1] < first[1]:
        print(f'{second[0]} {second[1]} es menor que {first[0]}{first[1]}')
    else:
        print('Son de la misma edad.')


if __name__ == '__main__':
    run()
