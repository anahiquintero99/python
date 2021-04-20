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
    value_pesos = 0.050
    country = 'Mexican'
    converter(value_pesos, country)

elif option == 2:
    value_pesos = 0.00028
    country = 'Colombian'
    converter(value_pesos, country)

elif option == 3:
    value_pesos = 0.011
    country = 'Argentine'
    converter(value_pesos, country)
else:
    print('Enter a correct option.')
