import re

f = open("day2.txt", "r")
lines = f.readlines()
f.close()
d = {"red": 12, "green": 13, "blue": 14}
count = 0
# lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
# "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
# "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
# "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
# "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
for line in range(100):
    lineNums = [int(x) for x in re.findall(r"\d+", lines[line])]
    if max(lineNums[1:]) > 14:
        pass
    else:
        # print(lines[line])
        # print(re.findall(r"(\d+)( blue)", lines[line]))
        blueNums = [int(x[0]) for x in re.findall(r"(\d+)( blue)", lines[line])]
        # print(blueNums)
        if max(blueNums) < 15:
            greenNums = [int(x[0]) for x in re.findall(r"(\d+)( green)", lines[line])]
            # print("1")
            if max(greenNums) < 14:
                redNums = [int(x[0]) for x in re.findall(r"(\d+)( red)", lines[line])]
                # print("2")
                if max(redNums) < 13:
                    count += line + 1
                    print("good")
print(count)