import re

f = open("day5.txt", "r")
lines2 = f.readlines()
lines = [x[:-1] for x in lines2]
f.close()

seedsa = [int(x) for x in lines[0].split(" ")[1:]]
seedsb = []
for x in range(0, len(seedsa), 2):
    seedsb += list(range(seedsa[x], seedsa[x]+seedsa[x+1]))
    print(x)
lines = lines[3:] + [""]
print(len(seedsb))

def mapping(lines, seedss):
    impor = lines.index("")
    if len(lines) > impor+1:
        print(lines[impor+1])
    ranges = []
    # maps = {}
    soils = []
    for x in range(impor):
        vals = [int(lin) for lin in lines[x].split(" ")]
        ranges += [vals]
    ranges.sort(key=lambda x:x[1])
    # print(seedss)
    # print(ranges)
    for seed in seedss:
        # print(seed)
        for rang in ranges:
            soils += [checkMap(rang[1], rang[2], rang[0], seed)]
    return [impor+2, soils]

def checkMap(rangStart, rangLength, rangMap, seed):
    if seed >= rangStart and seed < rangStart+rangLength:
        return seed - rangStart + rangMap
    return seed
# cats = list(filter(lambda x: True if len(x) > 0 and x[0] not in [str(num) for num in range(10)] else False, lines))
# # print(lines)
# print(cats)
# print(seedsb)
seed2soil = mapping(lines, seedsb)
lines = lines[seed2soil[0]:]
# print(seed2soil[1])
soil2fert = mapping(lines, seed2soil[1])
# print(lines[29:])
lines = lines[soil2fert[0]:]
# print(seeds)
# print(soil2fert[1])
fert2water = mapping(lines,soil2fert[1])
lines = lines[fert2water[0]:]
# print(fert2water[1])
# print(len(fert2water[1]))
water2light = mapping(lines,fert2water[1])
lines = lines[water2light[0]:]
# print(water2light[1])
# print(len(water2light[1]))
light2temp = mapping(lines,water2light[1])
lines = lines[light2temp[0]:]
# print(light2temp[1])
# print(len(light2temp[1]))
temp2humid = mapping(lines,light2temp[1])
lines = lines[temp2humid[0]:]
# print(temp2humid[1])
# print(len(temp2humid[1]))
humid2loc = mapping(lines,temp2humid[1])
# print(humid2loc[1])
# print(len(humid2loc[1]))
print(min(humid2loc[1]))
