import re
def t(text):
    a=re.findall("ab{2,3}",text)
    print(a)
with open("m.txt","r",encoding="utf-8")  as f:
    text=f.read()
    t(text)