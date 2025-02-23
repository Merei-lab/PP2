import re
def process_text(text):
    p=re.findall(r"\ba\w*?b\b",text)
    print(p)
   

with open("m.txt", "r", encoding="utf-8") as f:
    text = f.read()
    process_text(text)