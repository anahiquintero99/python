#definicion

class Person:

  def __init__ (self, name, age):
    self.name = name
    self.age = age
  
  def greeting(self, other_person):
    return f'Hola {other_person.name} me llamo {self.name}'
 
if __name__ == '__main__':
    person_1 = ('Anahi', 22)
    person_2 = ('Daniela', 7)
    
    print(person_1.greeting(person_2))