"""
x = lambda a : a + 10
print(x(5))
"""

"""
x = lambda a,b : a * b
print(x(3,4))
"""

#lambda with functionn

def func(n):
 return lambda a : a - n
myfunc=func(5)
print(myfunc(10))
