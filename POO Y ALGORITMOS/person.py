#definicion

class Person:

  def __init__ (self, name, age):
    self.name = name
    self.age = age
  
  def greeting(self, other_person):
    return f'Hola {other_person.name} me llamo {self.name}'