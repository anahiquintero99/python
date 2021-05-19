def divisors(num):
  divisors = []
  for i in range (1 , num + 1):
    if num % i == 0:
      divisors.append(i)
  return divisors

def run():
  try:
    num = int(input('Ingresa numero:'))
    print(divisors(num))
    print('Termino mi programa.')
    print(num)
  except ValueError:
    print('Solo se pueden ingresar numeros')
  

if __name__ == '__main__':
  run()