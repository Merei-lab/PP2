import re

def splitt(text):
 
  parts = re.split(r"(?=[A-Z])", text)
  return parts


with open("m.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(splitt(text))