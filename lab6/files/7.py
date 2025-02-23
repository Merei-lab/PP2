s = input()
d = input()
with open(s, 'r') as sf, open(d, 'w') as df:
    df.write(sf.read())