#python variables
w = 4       # x is of type int
w= "Sally" # x is now of type str
print(w)
#variable names
     #Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#assign multiple values
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#output variables
o = "Python "
p = "is "
i = "awesome"
print(o + p + i)
#global variables
e = "awesome"

def myfunc():
  e = "fantastic"
  print("Python is " + e)

myfunc()

print("Python is " + e)