"""
def scnd_max():
  

 list = [22,13,46,11,12,14,54]

 large=list[0]
 secondlargest=list[0]

 for x in range(1,len(list)):
  if list[x]>large:
     secondlargest=large
     large=list[x]
  elif list[x]>secondlargest:
     secondlargest=list[0]
    
 print(list)
 print(secondlargest)



scnd_max()
"""

#prime numbber
"""
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,14,15,16,17,18]

for i in range(1,len(list)):
 count=0
 for j in range(1,i+1):
  if(i%j==0):
   count=count+1
 if(count==2):
  print(i)
  print(j)
 
"""
n = 5
k = 2 * n - 1
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = n - 1

for i in range(n, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
