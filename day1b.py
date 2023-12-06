import re

f = open("day1a.txt", "r")
lines = f.readlines()
f.close()
tot = 0
nums = ["happy","one","two","three","four","five","six","seven","eight","nine"]
d = {}
for x in range(1,10):
    d[nums[x]] = x
    d[str(x)] = x
#lines = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
for line in lines:
    match1 = re.search("([0-9]|"+"|".join(nums)+")", line).group(0)
    match2 = re.search("([0-9]|"+"|".join([x[::-1] for x in nums])+")", line[::-1]).group(0)
    # print(match1, match2)
    # print(line, matches, d[matches[0]], d[matches[-1]])
    tot += d[match1]*10+d[match2[::-1]]
print(tot)