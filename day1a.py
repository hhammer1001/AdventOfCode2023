import re

f = open("day1a.txt", "r")
lines = f.readlines()
f.close()
tot = 0
for line in lines:
    tot += int(re.search("[0-9]", line).group(0))*10
    tot += int(re.search("[0-9]", line[::-1]).group(0))
print(tot)