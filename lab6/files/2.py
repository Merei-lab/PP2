import os

p = input()
e = os.path.exists(p)
r = os.access(p, os.R_OK)
w = os.access(p, os.W_OK)
x = os.access(p, os.X_OK)
print("exists:", e)
print("readable:", r)
print("writable:", w)
print("executable:", x)