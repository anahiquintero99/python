def run():

  #list
  my_list = [ 1, 'Hello', True, 4.5 ]
  #dictionary
  my_dict = {'fisrtname': 'Anahi', 'lastname': 'Quintero'}

    #Dictionary list
  super_list = [
      {'fisrtname': 'Anahi', 'lastname': 'Quintero'},
      {'fisrtname': 'Fernando', 'lastname': 'García'},
      {'fisrtname': 'Emilio', 'lastname': 'García'},
      {'fisrtname': 'Gabriela', 'lastname': 'García'},
  ]

  super_dict = {
      'natural_nums': [ 1, 2, 3, 4, 5],
      'integer_nums': [-1, 2, -3, 0, 6],
      'floating_nums': [1.1, 2.2, 3.3],
  }

  for key, value in super_dict.items():
      print(key , '-' , value)

  for element in super_list:
      print(element)

if __name__ == '__main__':
  run()