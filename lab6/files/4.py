f = input()
c = 0
with open(f, 'r') as fl:
    for l in fl:
        c += 1
print("lines:", c)