def run():
  text = 'qA2'
  print(any(map(lambda x: x.isalnum(), text)))
  print(any(map(lambda x: x.isalpha(), text)))
  print(any(map(lambda x: x.isdigit(), text)))
  print(any(map(lambda x: x.islower(), text)))
  print(any(map(lambda x: x.isupper(), text)))

if __name__ == '__main__':
  run()