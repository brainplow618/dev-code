"""
class person:
  def __init__(self,fname,lname):
    self.firstname=fname 
    self.lastname=lname
  
  def printname(self):
    print(self.firstname, self.lastname)
  
class student(person):
  pass
 
x = student("mike", "pomp")
x.printname()

"""
"""
class person:
  def __init__(self,fname,lname):
    self.firstname=fname 
    self.lastname=lname
  
  def printname(self):
    print(self.firstname, self.lastname)
  
class student(person):
  def __init__(self,fname,lname):
   person.__init__(self,fname,lname)
 
x = student("mike", "pomp")
x.printname()

"""

class person:
  def __init__(self,fname,lname):
    self.firstname=fname 
    self.lastname=lname
  
  def printname(self):
    print(self.firstname, self.lastname)
  
class student(person):
  def __init__(self,fname,lname,year):
   super().__init__(fname,lname) 
   self.passyear = year
   
x = student("mike", "pomp", 2009)
print(x.passyear)







