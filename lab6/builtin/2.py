
str="HKJ hg jgjGJBJH jh  ,/"
up=0
lou=0
for i in str:
    if i.isupper():
        up+=1
    elif i.islower():
        lou+=1
    
print(f"upper{up},\nlower{lou}")