
def run():
  #square = []
  #for i in range(1, 101):
  #  if i % 3 != 0:
  #    square.append(i ** 2)

  #List comprehensions
  
  print('EXERCISE ONE\n')
  square = [ i**2 for i in range(1, 100) if i % 3 != 0]
  print(square)
  
  print('EXERCISE TWO\n')
  multiplo = 2*2*3*3
  multiples = [i for i in range(1, 10000) if i % multiplo == 0]
  print(multiples)
  
if __name__ == '__main__':
  run()

