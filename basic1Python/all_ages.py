
def run():
    first_people = []
    name = input('What is your name?: ')
    first_people.append(name)
    years = int(input('How old are you?: '))
    first_people.append(years)

    second_people = []
    name = input('What is your name?: ')
    second_people.append(name)
    years = int(input('How old are you?: '))
    second_people.append(years)

    if second_people[1] > first_people[1]:
        print(f'{second_people[0]} es mayor de edad que {first_people[0]}')
    elif second_people[1] < first_people[1]:
        print(f'{second_people[0]} es menor de edad que {first_people[0]}')
    else:
        print('Son de la misma edad.')


if __name__ == '__main__':
    run()
