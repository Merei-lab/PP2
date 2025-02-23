import os

p = input()
if os.path.exists(p):
    fn = os.path.basename(p)
    dn = os.path.dirname(p)
    print("file name:", fn)
    print("dir name:", dn)