import re

f = open("day3.txt", "r")
lines2 = f.readlines()
lines = [x[:-1] for x in lines2]
f.close()
tot = 0
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
                nums[line][-1][2] = ind
                nums[line] += [["", 0,0]]
        elif lines[line][ind] in "0123456789":
            nums[line][-1][0] += lines[line][ind]
            if not num:
                num = True
                nums[line][-1][1] = ind-1
        else:
            if num:
                num = False
                nums[line][-1][2] = ind
                nums[line] += [["", 0,0]]
            chars[line] += [ind]
    nums[line] = nums[line][:-1]
charSet = set()
for line in range(140):
    print(line)
    for numSet in nums[line]:
        print(charSet)
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
                    counted = True
print(tot)