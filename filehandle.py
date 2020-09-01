#f = open("/home/shami/Desktop/python/shami.txt", "r")
#print(f.read())
#print(f.read(5))

#print(f.readline())
#print(f.readline())


#for x in f:
 #print(x)
 
 
#python file create and write
"""
f = open("/home/shami/Desktop/python/shami.txt","a")
f.write("Something add in file shami")
f.close()
f = open("/home/shami/Desktop/python/shami.txt", "r")
print(f.read())
"""


""" 
f = open("/home/shami/Desktop/python/shami.txt","w")
f.write("Ooops ,i del")
f.close()

f = open("/home/shami/Desktop/python/shami.txt", "r")
print(f.read())
"""
#delet file

"""
import os
os.remove("/home/shami/Desktop/python/shami.txt")
"""

import os
if os.path.exists("/home/shami/Desktop/python/shami.txt"):
  os.remove("/home/shami/Desktop/python/shami.txt")
else:
  print("The file does not exist")
