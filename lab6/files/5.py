l = input().split()
f = input()
with open(f, 'w') as fl:
    for i in l:
        fl.write(i + '\n')