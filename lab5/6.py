import re
def process_text(textt):
    
    for char in " ,.":
        textt = textt.replace(char, ":")
    return textt


with open("m.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(process_text(text))
