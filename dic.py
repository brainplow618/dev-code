"""
dic={
	"brand":"bata",
	"model":"must",	
	"year":2000
}
print(dic)
"""
"""
dic={
	"brand":"bata",
	"model":"must",	
	"year":2000
}

#x=dic["model"]
#x=dic.get("model")
x=dic["year"]=2020
print(x)
"""
#Loop through a dic.
"""
dic={
	"brand":"bata",
	"model":"must",	
	"year":2000
}
"""
#for x in dic:
#print(dic[x])
#for x in dic.values():
 #  print(x)


#select item
"""
dic={
	"brand":"bata",
	"model":"must",	
	"year":2000
}
for x,y in dic.items():
 print(x,y)
 """
 
#check if key exist
"""
dic={
	"brand":"bata",
	"model":"must",	
	"year":2000
}
if "model" in dic:
 print("yes!")
 """
 
#dic length
"""
dic={
	"brand":"bata",
	"model":"must",	
	"year":2000
}
print(len(dic))
"""

#add item

"""

dic={
	"brand":"bata",
	"model":"must",	
	"year":2000
}
dic["color"]="red"
print(dic)
"""
#pop
"""
dic={
	"brand":"bata",
	"model":"must",	
	"year":2000
}
#dic.pop("model")
#dic.popitem()
#del dic["model"]
#del dic
#dic.clear()
mydic=dic.copy()
print(mydic)
#print(dic)


"""


#Nested dic
"""
myfamily={
	"child1":{
	"name":"email",
	"age":2000
 },
 	"child2":{
 	"name":"google",
 	"age":2004
 },
 	"child3":{
 	"name":"yahoo",
 	"age":2008
 }

}
print(myfamily)
"""
"""
child1={
	"name":"yahoo",
	}
child2={
	"name":"google",
	}
child3={
	"name":"mail"
	}
	
myfamily={
	"child1":child1,
	"child2":child2,
	"child3":child3
	}
print(myfamily)
"""
#the dict() Constructor

dic = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(dic)


















































































































































































































