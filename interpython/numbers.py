

def isalum_value(s):
  list_s = list(s)
  for i in list_s:
    if i.isalnum() == True:
      return True
    else:
      return False

def isalpha_value(s):
  list_s = list(s)
  for i in list_s:
    if i.isalpha() == True:
      return True
    else:
      return False

def isdigit_value(s):
  list_s = list(s)
  for i in list_s:
    if i.isdigit() == True:
      return True
    else:
      return False
      continue


def run():
  s = 'qA2'
  print(isalum_value(s))
  print(isalpha_value(s))
  print(isdigit_value(s))

if __name__ == '__main__':
  run()