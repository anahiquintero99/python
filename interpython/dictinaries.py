import math

def run():
  print('EXERCISE ONE\n')
  multiplo = 2*2*3*3
  multiples = {num:num for num in range(1, 99999) if num % multiplo == 0}
  print(multiples)

  print('EXERCISE TWO\n')
  square = {i:math.sqrt(i) for i in range(1, 1000)}
  print(square)
  

if __name__ == '__main__':
  run()