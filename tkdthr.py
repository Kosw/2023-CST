class Animal:
  def __init__(self, age, name):
    self.age=age
    self.name=name
    
  def get_age(self):
    return self.age
  
  def get_name(self):
    return self.name
  
  def __str__(self):
    return "<"+self.name+":"+str(self.age)+">"

class Cat(Animal):
    def speak(self):
        print("Meow")
        
    def feature(self):
        return "Cute"

    def __str__(self):
        return "<" + self.name + ":" + str(self.age) + ":" + self.feature() + ">"