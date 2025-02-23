import re 
text="AaaAAaBbbBBCCCcc"
t=re.sub(r"(?!^)(?=[A-Z])"," ",text) 
print(t)