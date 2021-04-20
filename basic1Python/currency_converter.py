menu = """
Welcome to the currency converter
  
  1.-Mexican Pesos
  2.-Colombian Pesos
  3.-Argentine Pesos

  Choose an option:  """

option = int(input(menu))


def converter(value_pesos, country):
    pesos = float(input('Enter amount: '))
    dollars = value_pesos * pesos
    print(f'{country} Pesos: {pesos} = {round(dollars, 2)} dollars')


if option == 1:
    converter(0.050, 'Mexican')

elif option == 2:
    converter(0.00028, 'Colombian')

elif option == 3:
    converter(0.011, 'Argentine')
else:
    print('Enter a correct option.')
