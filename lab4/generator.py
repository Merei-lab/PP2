#1

a=10
gen=(i**2  for i in range(1,10))
for i in range(a-1):
    print(next(gen))


#2
n =int(input("entr N  "))
def gene(n):
    for i in range(0,n+1,2):
        yield i
gen = gene(n)
for value in gen:
    print(value)  


#3
def ge(n):
  
  for i in range(n + 1):
    if i % 3 == 0 and i % 4 == 0:
      yield i
n = 50
for i in ge(n):
  print(i)


#4
a=2
b=10
def sq(a,b):
   for i in range (a,b+1):
      yield i**2
for i in sq(a,b):
   print(i)

#5

def rev(n):
  
  while n >= 0:
    yield n
    n -= 1


for i in rev(10):
  print(i)