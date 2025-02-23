import re 
text="AaaAAaBbbBBCCCcc"
t=re.sub(r"(?!^)(?=[A-Z])","_",text).lower() 
print(t)