#Python Tuples
#One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#ACCES TUPLES
#This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#UPDATE TUPLES
#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#UNPACK TUPLES
#Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#LOOP 
#Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#JOIN 
#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#multipiy
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#METHODS
ppp=(2005,2006,2005,2007)
print(ppp.count(2005))
print(ppp.index(2005))