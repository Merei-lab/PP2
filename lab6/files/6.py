import string

for l in string.ascii_uppercase:
    f = l + ".txt"
    open(f, 'w').close()