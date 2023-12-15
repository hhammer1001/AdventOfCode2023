import re

f = open("day3.txt", "r")
lines2 = f.readlines()
lines = [x[:-1] for x in lines2]
f.close()
tot = 0
tots = [[0] for x in range(140)]
nums = [[["", 0,0]] for x in range(140)]
chars = [[] for x in range(140)]
# print(lines2[0])
# print(lines[0])
# print(nums)
# for line in range(len(lines)):
for line in range(140):
    # print(lines[line])
    # n = 0
    num = False
    for ind in range(len(lines[line])):
        if lines[line][ind] == ".":
            if num:
                # n += 1
                num = False
                nums[line][-1][2] = ind-1
                nums[line] += [["", 0,0]]
        elif lines[line][ind] in "0123456789":
            if not num:
                num = True
                nums[line][-1][1] = ind
        else:
            if num:
                num = False
                nums[line][-1][2] = ind-1
                nums[line] += [["", 0,0]]
            chars[line] += [ind-1, ind, ind+1]
    if nums[line][-1][0] == "":
        nums[line] = nums[line][:-1]
    elif num:
        nums[line][-1][2] = 139
charSet = set()
for line in range(140):
    print(nums[line])
    for numSet in nums[line]:
        # print(charSet)
        counted = False
        for i in range(numSet[1], numSet[2] + 1):
            if not counted:
                charSet = set(chars[line])
                if line > 0:
                    charSet.update(chars[line - 1])
                if line < 139:
                    charSet.update(chars[line + 1])
                if i in charSet:
                    tot += int(numSet[0])
                    tots[line][0] += int(numSet[0])
                    counted = True
print(tot)

# import re
# from collections import defaultdict
# from math import prod

# with open("day3.txt") as f:
#     lines = f.read().split("\n")

# # building symbols grid as {xy_position: symbol}
# symbols = dict()
# for y, line in enumerate(lines):
#     for x, c in enumerate(line):
#         if c not in "1234567890.":
#             symbols[(x, y)] = c

# # checking if a number has a rectangular neighborhood containing a symbol and
# # building a gear grid as {gear_position: [part numbers list]}
# vals = [[0] for x in range(140)]
# gears = defaultdict(list)
# part_numbers_sum = 0
# for y, line in enumerate(lines):
#     for match in re.finditer(r"\d+", line):
#         for (s_x, s_y), c in symbols.items():
#             if (match.start() - 1 <= s_x <= match.end()) and (y - 1 <= s_y <= y + 1):
#                 num = int(match.group())
#                 vals[y][0] += num
#                 part_numbers_sum += num
#                 if c == "*":
#                     gears[(s_x, s_y)].append(num)
#                 break

# for x in vals:
#     print(x)