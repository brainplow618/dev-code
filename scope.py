"""
def myfunc():
 x=300
 print(x)
 
myfunc()
"""

#function inside function
"""
def myfunc():
 x = 300
 def myinnerfunc():
  print(x)
 myinnerfunc()
myfunc()
"""

#naming function
"""
x=300
def myfunc():
 x=200
 print()
myfunc()
print(x)
"""
import mymodule

mymodule.greeting("Jonathan")

