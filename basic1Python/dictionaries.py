def run():
    my_dictionary = {
        'Anahi': 'Quintero',
        'Gabriela': 'Garcia',
        'Fernando': 'Garcia',
    }
    print(my_dictionary['Anahi'])

    for name in my_dictionary.keys():
        print(name)

    for name in my_dictionary.values():
        print(name)

    for name, last_name in my_dictionary.items():
        print(name + ' ' + last_name)


if __name__ == '__main__':
    run()
