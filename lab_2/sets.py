#Python sets

#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)


#Access the set items
#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


#Add items
#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


#Rempve item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


#Loop sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#Join sets
#The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)


#Set methods
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}
print(set1.issubset(set2))