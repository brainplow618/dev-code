# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print(j,end=' ')
#
#     print("\r")
#
# n = 5
# for i in range(0,n):
#     for j in range(0,i + 1):
#         print(i,end=' ')
#
#     print("\r")
#
# row = 5
# b = 0
# for i in range(row,0,-1):
#     b += 1
#     for j in range(1,i + 1):
#         print(b, end=' ')
#     print("\r")
#
# row = 5
# for i in range(row,0,-1):
#     for j in range(1,i + 1):
#         print("*", end=' ')
#     print("\r")
#
#
#
# row = 5
# for i in range(0,row):
#     for j in range(0,i + 1):
#         print("*",end=' ')
#     print("     ")
#
# print(" ")
#
# for i in range(row,0,-1):
#     for j in range(0,i - 1):
#         print("*",end=' ')
#     print(" ")
#
#
# row = 5
# k = 2 * row - 2
# for i in range(0, row):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0,i + 1):
#         print("* ", end="")
#     print("")
#
# row1 = 5
# l = row1 - 2
# for a in range(row1,-1,-1):
#     for b in range(l,0,-1):
#         print(end=" ")
#     l = l + 1
#     for b in range(0 ,a + 1):
#         print("* ",end="")
#     print("")
#
# row = 5
# k = 2 * row - 2
# for i in range(0,row):
#     for j in range(0,k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0,i + 1):
#         print("* ",end="")
#     print("")
#
# row1 = 5
# l = row1 - 1
# for a in range(row1,-1,-1):
#     for b in range(l,0,-1):
#         print(end=" ")
#     l = l + 1
#     for b in range(1,a + 1):
#         print("* ",end="")
#     print("")
#


#
# list = [32,342,23,32412,455]
# max_num = list[0]
# for x in range(1,len(list)):
#     if list[x] > max_num:
#         max_num = list[x]
# print(max_num)
#
#
# list1 = [23,23,41,12,12]
# max = 0
# for i in list1:
#     if i > max:
#         max = i
# print(max)

#
# print("print the value of range")
# for i in range(6):
#     print(i,end=" , ")

# n = 2
# for i in range(1,11,1):
#     product = n*i
#     print(i ,":" , product)
#
# list = [5,15,23,45,54,25]
# for i in list:
#     if (i % 5 == 0):
#         print(i)
#
# list = [10,20,30,40,50]
#
# for x in range(len(list) - 1,-1,-1):
#     print(list[x])
#
# for x in range(-10,0,1):
#     print(x)
#
# for i in range(5):
#     print(i)

# for char in range ('a','z'):
#     print(char)
#
# numbers = [10, 20]
# items = ["Chair", "Table"]
# #
# for x in numbers:
#   for y in items:
#     print(x, y)
#
# samplstr = "this is python python is programming language"
# cnt = samplstr.count("python")
# print("python appened",cnt,"time")

# num1 = int(input("Enter first no."))
# num2 = int(input("Enter seconf no."))
# result = num1 * num2
# print("\n")
# print("product is ",result)
#
# print('my','name','is','shami',sep=" ** ")


# print('%o,' % (8))

# num = float(input("ENter a number:"))
# print(num)

# floatNumbers = []
# n = int(input("Enter the list size : "))
#
# str1, str2, str3 = input("Enter three string:").split()
# print(str1, str2, str3)
#
# money = 1000
# qty = 3
# prise = 450
#
# print("I have ",money,"and i buy ",qty,"football","in ",prise)

import os
# for num in range(1,11):
#     print(num)
#
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# i = 5
# for x in range(1,i):
#     for y in range(1,x + 1):
#         print(y,end=" ")
#     print("")

# n = int(input("Enter number for print table:"))
# for i in range(1,11):
#     print(n," * ",i,"=",n * i)
#
# list = [12,15,22,25,55,65,44,111,125,100,520,250]
# for x in list:
#     if (x > 150):
#         break
#     if (x % 5 == 0):
#         print(x)


#
# num = 32545
# c = 0
# while num != 0:
#     num //=10
#     c += 1
# print("print the count number:",c)
#
# str1, str2, str3 = input("Enter three string").split()
# print(str1, str2, str3)

# n = 1
# while n <= 10:
#     print(n)
#     n += 1


# n = 6
# for i in range(1,n):
#     for j in range(1,i + 1):
#         print(j,end=' ')
#     print(" ")


# n = 2
# for i in range(1,11):
#     c = n*i
#     print(c)

# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# for i in list1:
#     if (i > 150):
#         break
#     if (i%5==0):
#         print(i)

# n = -10
# for i in range(n,0,1):
#     print(i)
# else:
#     print("Done!")
#
# def demo(name,age):
#     print(name,age)
# demo("shami",24)
#
# def fun1(*args):
#     for i in args:
#         print(i)
#
# fun1(23,24,34)
# fun1(3,2,3)
#
# def calculation(a,b):
#     return a+b,a-b,a*b,a/b,a%b
#
# re=calculation(25,25)
# print(re)

def empolyee(name,salary=9000):
    print("Empolyee=",name,"salary=",salary)

# empolyee("shami",9000)
# empolyee("fahad")
# empolyee("ali")
#
# def sum():
#
#     a = 0
#     for i in range(1,11):
#        a = a + i
#     print(a)
# sum()
#
# def disply(name,age):
#     print(name,age)
#
#
# new = disply
# disply("shami",23)
# disply("new",43)


# for i in range(4,30,2):
#     print(i)

# aList = [4, 6, 8, 24, 12, 2]
# max = 0
# for i in aList:
#     if i > max:
#         max = i
# print(max)

# listOne = [3, 6, 9, 12, 15, 18, 21]
# listTwo = [4, 8, 12, 16, 20, 24, 28]
# listThree = list()
#
# oddElements = listOne[1::2]
# print("Element at odd-index positions from list one")
# print(oddElements)
#
# EvenElement = listTwo[0::2]
# print("Element at even-index positions from list two")
# print(EvenElement)
#
# print("Printing Final third list")
# listThree.extend(oddElements)
# listThree.extend(EvenElement)
# print(listThree)

# samplelist = [23,3,35,676,23,2]
#
# print(samplelist)
# element = samplelist.pop(4)
# print(samplelist)
#
# element = samplelist.insert(2,element)
# print(samplelist)
#
# samplelist.append(element)
# print(samplelist)

# list = [2,3,4,6,2,2,3,5,6,7,8,6,5,4,3,3,5,6,7]
#
# print("Original list",list)
#
# countdict = dict()
#
# for item in list:
#     if(item in countdict):
#         countdict[item] += 1
#     else:
#         countdict[item] = 1
# print("Printing count of each item",countdict)

# flist = [1,2,3,4,5,6]
# llist = [2,4,6,8,10,12]
#
# print("First list",flist)
# print("last list",llist)
#
# result = zip(flist,llist)
# resultset = set(result)
# print(resultset)

# fset = {23,34,56,67,76,44,33,45,22}
# sset = {23,34,66,77,88,99,44,21,11}
#
# inter = fset.intersection(sset)
# print("Intersection element",inter)
#
# for item in inter:
#     fset.remove(item)
# print(fset)

# rollno = [23,22,33,44,55,66,77,32]
# sampledic = {'jhon':23, 'smith':22, 'kelly':55, 'jason':32}
#
# print("list",rollno)
# print("Dictoinary:",sampledic)
#
# rollno[:]=[item for item in rollno if item in sampledic.values()]
# print("after removing:",rollno)

# speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
# print("Dictionary vlues:",speed.values())
#
# speedlist = list()
#
# for item in speed.values():
#     if item not in speedlist:
#         speedlist.append(item)
# print("Unique list",speedlist)

# sampllist = [23,33,4,44,55,66,77,77,77,44,44,55,55,88,88,99]
#
# # newset = set(sampllist)
# newtuple =list(tuple(sampllist))
# print(newtuple)
#
# max = 0
# for i in newtuple:
#     if i > max:
#         max = i
# print(max)
#
# min = newtuple[0]
# for j in newtuple:
#     if j < min:
#         min = j
# print(min)



# keys = ['jhon','smith','jerry','clay']
# values = [1,2,3,4]
#
# output = dict(zip(keys,values))
# print("Dictionary:",output)

# dic1 = {'ten':10, 'twenty':20, 'thirty':30}
# dic2 = {'forty':40, 'fifty':50, 'sixty':60}
#
# new = {**dic1 , **dic2}
#
# print(new)

# sampldict = {
#     "class":{
#         "student":{
#             "name":"Mike",
#             "marks":{
#                 "physics":66,
#                 "History":80
#
#             }
#         }
#     }
# }
# print(sampldict['class']['student']['marks']['History'])

# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
#
# newrec = dict.fromkeys(employees, defaults)
# # print(newrec)
# print(newrec["Kelly"])
#
# sampledict = {
#     "name":"Shami",
#     "ID":12,
#     "Salary":5000,
#     "AppType":"DevOps",
#     "city":"FSD"
#
# }
#
# keys = ["name","Salary"]
#
# newdict = {k: sampledict[k] for k in keys}
# print(newdict)

# sampledict = {
#     "name":"Shami",
#     "ID":12,
#     "Salary":5000,
#     "AppType":"DevOps",
#     "city":"FSD"
#
# }
#
# keystoremove = ["name","ID"]
#
# new = {k: sampledict[k] for k in sampledict.keys() - keystoremove}
# print(new)

# sampledict = {'a':10, 'b':20, 'c':30}
# print(10 in sampledict.values())

# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# sampleDict['location'] = sampleDict.pop('city')
# print(sampleDict)

# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
#
# print(min(sampleDict, key=sampleDict.get))

# sample = {
#     'emp1': {'name':'ali', 'salary':2000},
#     'emp2': {'name':'shami', 'salary':2500},
#     'emp3': {'name':'saud', 'salary':6000}
# }
#
# sample['emp2']['salary'] = 8000
# print(sample)

# set = {'yellow','green','blue'}
# list = ['red','pink','white']
#
# set.update(list)
# print(set)

# st1 = {10,20,30,40,50}
# st2 = {40,50,60,70,80}
# # print(st1.intersection(st2))
# # print(st1.union(st2))
#
# newset = st1.intersection(st2)
# print(newset)

# set = {10,20,30,40,50}
# set.difference_update({10,20,30})
# print(set)
#
# st1 = {10,20,30,40,50}
# st2 = {40,50,60,70,80}
# # set = st1.symmetric_difference(st2)
# # print(set)
#
# if st1.isdisjoint(st1):
#     print("Two set has not common element")
# else:
#     print("Tow set has common element:")
#     print(st1.intersection(st2))

# set1 = {10,20,30,40,50}
# set2 = {40,50,60,70,80}
#
# set1.symmetric_difference_update(set2)
# print(set1)

# list(input(list))
# print(list)

# tuple = (12,23,4,5,66,77)
# tuple = tuple[::-1]
# print(tuple)


# aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
# print(aTuple[1][2])

# tuple = (50, )
# print(tuple)


# tuple = (10,20,30,40)
# a,b,c,d = tuple
# print(a)
# print(b)
# print(c)
# print(d)

# tuple1 = (11,22)
# tuple2 = (33,44)
# tuple1,tuple2 = tuple2,tuple1
# print(tuple1)
# print(tuple2)

# tuple1 = (11,22,33,44,55,66)
# tuple2 = tuple1[3:-1]
# print(tuple2)
# import json
# data = {"key1":"value1","key2":"value2"}
# jsondata = json.dumps(data)
# print(data)

# import random
# print("print number between 100 to 999 which is divisble by 5")
# for num in range(3):
#     print(random.randrange(100,999,5),end=' ')
#

max = 0
list = [23,2,4,66,77]
for x in list:
    if x > max:
        max = x
print(max)
