import os
dire=[]
file=[]
items=[]
dire=os.listdir(".")
for i in dire:
    item_path = os.path.join(".", i)

    if os.path.isdir(item_path):
        dire.append(i)
    elif os.path.isfile(item_path):
        file.append(i)

    items.append(i)
print(dire)
print(file)
print(items)
#a=os.path.isdir(s=".")
#print(a)