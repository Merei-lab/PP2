import os

p = input()
if os.path.exists(p) and os.access(p, os.W_OK):
    os.remove(p)