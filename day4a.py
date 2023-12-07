import re

f = open("day4.txt", "r")
lines2 = f.readlines()
lines = [x[:-1] for x in lines2]
f.close()

cards = []
winners = []
tot = 0
for line in lines:
    line = line.split(":")[1]
    numSet = line.split("|")
    cards += [set(re.findall(r"\d+",numSet[1]))]
    winners += [set(re.findall(r"\d+",numSet[0]))]

for cardNum in range(len(cards)):
    count = -1
    for num in cards[cardNum]:
        if num in winners[cardNum]:
            count += 1
    if count > -1:
        tot += pow(2, count)
print(tot)