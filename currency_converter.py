menu = """
Welcome to the currency converter
  
  1.-Mexican Pesos
  2.-Colombian Pesos
  3.-Argentine Pesos

  Choose an option:  """

option = int(input(menu))

if option == 1:
    mexican_pesos = float(input('Enter amount: '))
    value_mexican = 0.050
    dollars = value_mexican * mexican_pesos
    print(f'Mexican pesos: {mexican_pesos} = {round(dollars, 2)} dollars')

elif option == 2:
    colombian_pesos = float(input('Enter amount: '))
    value_colombian = 0.00028
    dollars = value_colombian * colombian_pesos
    print(f'Colombian pesos: {colombian_pesos} = {round(dollars, 2)} dollars')

elif option == 3:
    argentine_pesos = float(input('Enter amount: '))
    value_argentine = 0.011
    dollars = value_argentine * argentine_pesos
    print(f'Mexican pesos: {argentine_pesos} = {round(dollars, 2)} dollars')

else:
    print('Enter a correct option.')
