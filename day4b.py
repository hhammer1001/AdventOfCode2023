import re

f = open("day4.txt", "r")
lines2 = f.readlines()
lines = [x[:-1] for x in lines2]
f.close()


# lines = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
cards = []
winners = []
tots = [0 for i in range(201)]
amts = [1 for i in range(300)]
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
        for times in range(amts[cardNum]):
            tots[cardNum] = pow(2, count)
            for x in range(count + 1):
                amts[cardNum + x + 1] += 1

for i in range(201):
    tot += amts[i]


# print(amts)

# print(tots)

print(tot)

