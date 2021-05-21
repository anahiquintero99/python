def factory(n):
  print(n)
  if n == 1:
    return 1

  return n * factory(n-1)

n = int(input('Escribe entero: '))

print(factory(n))