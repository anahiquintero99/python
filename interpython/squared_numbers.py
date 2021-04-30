
def run():
  #square = []
  #for i in range(1, 101):
  #  if i % 3 != 0:
  #    square.append(i ** 2)

  #List comprehensions
  
  #square = [ i**2 for i in range(1, 101) if i % 3 != 0]
  #print(square)

  multiplo = 2*2*3*3
  #multiples = [i for i in range(1, 99999) if i % multiplo == 0]
  #print(multiples)

  multiples = {num:num for num in range(1, 99999) if num % multiplo == 0}
  print(multiples)
  
if __name__ == '__main__':
  run()

