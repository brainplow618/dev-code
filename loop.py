#while loop
"""
i = 1
while i < 6:
 print(i)
 i+=1
 """
#break statement
"""
i = 1
while i < 6:
 print(i)
 if i==4:
  break
 i += 1
 """
#continue
"""
i = 0
while i < 6:
 i += 1
 if i==3:
  continue
 print(i)
 """
#else with  while
"""
i = 0
while i<6:
 print(i)
 i += 1
else:
 print("i is longer less than 6")
"""

#For_Loop
"""
fruite = ["banana","apple","mango"]
for x in fruite:
 print(x)
"""
"""
for x in "banana":
 print(x)
"""
 
#breat stat. with for loop
"""
fruite = ["banana","apple","mango"]
for x in fruite:
 print(x)
 if x == "apple":
  break
 """
""" 
fruite = ["banana","apple","mango"]
for x in fruite:
 if x == "apple":
  break
 print(x)
"""
"""
fruite = ["banana","apple","mango"]
for x in fruite:
 if x == "banana":
  continue
 print(x)

"""

#Range() function
"""
for x in range(5):
 print(x)
"""
"""
for x in range(2,6):
 print(x)
 """
"""
for x in range(2,20,2):
 print(x)
 """
 
#else_with for loop
"""
for x in range(5):
 print(x)
else:
 print("loop finish")
 """
 
#nested loop with for

"""
con = ["a","b","c","d","e"]
fruit = ["red","blue","green","black","pink"]

for x in con:
 for y in fruit:
   print(x,y)

 
 """
 """
for x in [1,2,3,]:
 pass
 """
 

