import re
with open("../input/raw-text.txt") as f:
    text = f.read()
x = re.findall(r"[A-Za-z0-9.]+@[A-Za-z0-9.-]+\.[A-Za-z0-9.]+\.?(?:[A-Za-z0-9.]+)", text)
print(x)