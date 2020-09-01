"""
class myclass:
 x=5
print(myclass)
"""
"""
class myclass:
 x=5
p1=myclass()
print(p1.x)
"""
"""
class person:
 def __init__(self,name,age):
  self.name = name
  self.age = age

p1=person("john",36)

print(p1.name)
print(p1.age)
"""

"""
class person:
 def __init__(self,name,age):
  self.name = name
  self.age = age

 def myfunc(self):
  print("Hello is my name is " + self.name)
  
p1=person("john",22)
p1.myfunc()

"""
"""
class person:
 def __init__(first,name,age):
  first.age = age
  first.name = name
  

 def myfunc(abc):
  print("Hello is my name is " + abc.name)
  
p1=person("john",22)
#p1.myfunc()
p1.age=40
print(p1.age)

"""
"""
class person:
 def __init__(first,name,age):
  first.age = age
  first.name = name
  

 def myfunc(abc):
  print("Hello is my name is " + abc.name)
  
p1=person("john",22)
del p1.age
print(p1.age)
"""

