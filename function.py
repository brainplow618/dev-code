"""
def my_func():
 print("print hello from myfunction")
my_func()
"""
"""
def my_func(fname):
 print(fname + " reference")
 
my_func("Email")
my_func("ID")
my_func("address")
"""

"""
def my_func(fname,lname):
 print(fname +" "+ lname)
 
my_func("Email","Refernce")
"""
"""
def my_func(**kids):
 print("His last name is " + kids["lname"])


my_func(fname="tobies", lname="ali")
"""
"""
def my_func(country="pakistan"):
 print("I am from "+country)
my_func("Sweden")
my_func("UAE")
my_func()
my_func("Brazil")

"""
"""
def my_func(food):
 for x in food:
  print(x)
  
fruit=["mango","apple","banana"]
my_func(fruit)
"""

#Return value

def func(x):
 return 5 * x
 
print(func(3))
print(func(5))
print(func(6))
