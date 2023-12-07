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
gears = {}
for line in range(140):
    # print(lines[line])
    # n = 0
    num = False
    for ind in range(len(lines[line])):
        if lines[line][ind] == ".":
            if num:
                # n += 1
                num = False
                nums[line][-1][2] = ind
                nums[line] += [["", 0,0]]
        elif lines[line][ind] in "0123456789":
            nums[line][-1][0] += lines[line][ind]
            if not num:
                num = True
                nums[line][-1][1] = ind - 1
        else:
            if num:
                num = False
                nums[line][-1][2] = ind
                nums[line] += [["", 0,0]]
            chars[line] += [ind]
    if nums[line][-1][0] == "":
        nums[line] = nums[line][:-1]
    elif num:
        nums[line][-1][2] = 139
charSet = [set(chars[x]) for x in range(140)]
for line in range(140):
    print(nums[line])
    for numSet in nums[line]:
        # print(charSet)
        gear = False
        for i in range(numSet[1], numSet[2] + 1):
            if line > 0:
                if i in charSet[line - 1]:
                    gear = True
                    if (line-1, i) in gears:
                        gears[(line-1, i)] += [int(numSet[0])]
                    else:
                        gears[(line-1, i)] = [int(numSet[0])]
            if not gear and line < 139:
                if i in charSet[line + 1]:
                    gear = True
                    if (line+1, i) in gears:
                        gears[(line+1, i)] += [int(numSet[0])]
                    else:
                        gears[(line+1, i)] = [int(numSet[0])]
            if not gear:
                if i in charSet[line]:
                    if (line, i) in gears:
                        gears[(line, i)] += [int(numSet[0])]
                    else:
                        gears[(line, i)] = [int(numSet[0])]
for key in gears:
    if len(gears[key]) == 2:
        tot+= gears[key][0]*gears[key][1]
print(tot)
