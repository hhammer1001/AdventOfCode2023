import re

f = open("day5.txt", "r")
lines2 = f.readlines()
lines = [x[:-1] for x in lines2]
f.close()

seeds = [int(x) for x in lines[0].split(" ")[1:]]
lines = lines[3:] + [""]
# seed2soilranges = []
# seed2soilmaps = {}
# for x in range(29):
#     vals = [int(lin) for lin in lines[x].split(" ")]
#     seed2soilranges += [vals]
# seed2soilranges.sort(key=lambda x:x[0])
# soils = []
# for seed in seeds:
#     # print(seed)
#     for rang in seed2soilranges:
#         if seed >= rang[0]:
#             if seed < rang[0] + rang[2]:
#                 seed2soilmaps[seed] = seed - rang[0] + rang[1]
#                 soils += [seed - rang[0] + rang[1]]
#                 break
#         else:
#             seed2soilmaps[seed] = seed
#             soils += [seed]
#             break
# lines = lines[31:]
# soil2fertranges = []
# soil2fertmaps = {}
# for x in range(19):
#     vals = [int(lin) for lin in lines[x].split(" ")]
#     soil2fertranges += [vals]
# soil2fertranges.sort(key=lambda x:x[0])
# ferts = []
# for soil in soils:
#     # print(seed)
#     for rang in soil2fertranges:
#         if soil >= rang[0]:
#             if soil < rang[0] + rang[2]:
#                 soil2fertmaps[seed] = soil - rang[0] + rang[1]
#                 ferts += [soil - rang[0] + rang[1]]
#                 break
#         else:
#             seed2soilmaps[soil] = soil
#             ferts += [soil]
#             break

# lines = lines[21:]

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
        done = False
        # print(seed)
        for rang in ranges:
            # print(seed, rang)
            if seed >= rang[1]:
                if seed < rang[1] + rang[2]:
                    # print(seed, rang,[seed - rang[1] + rang[0]])
                    # maps[seed] = seed - rang[0] + rang[1]
                    soils += [seed - rang[1] + rang[0]]
                    done = True
                    break
            else:
                # maps[seed] = seed
                soils += [seed]
                done = True
                break
        if not done:     
            soils += [seed]
    return [impor+2, soils]

# cats = list(filter(lambda x: True if len(x) > 0 and x[0] not in [str(num) for num in range(10)] else False, lines))
# # print(lines)
# print(cats)
seed2soil = mapping(lines, seeds)
lines = lines[seed2soil[0]:]
print(seed2soil[1])
soil2fert = mapping(lines, seed2soil[1])
# print(lines[29:])
lines = lines[soil2fert[0]:]
# print(seeds)
print(soil2fert[1])
fert2water = mapping(lines,soil2fert[1])
lines = lines[fert2water[0]:]
print(fert2water[1])
# print(len(fert2water[1]))
water2light = mapping(lines,fert2water[1])
lines = lines[water2light[0]:]
print(water2light[1])
# print(len(water2light[1]))
light2temp = mapping(lines,water2light[1])
lines = lines[light2temp[0]:]
print(light2temp[1])
# print(len(light2temp[1]))
temp2humid = mapping(lines,light2temp[1])
lines = lines[temp2humid[0]:]
print(temp2humid[1])
# print(len(temp2humid[1]))
humid2loc = mapping(lines,temp2humid[1])
print(humid2loc[1])
# print(len(humid2loc[1]))
print(min(humid2loc[1]))
