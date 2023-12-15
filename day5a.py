import re

f = open("day5.txt", "r")
lines2 = f.readlines()
lines = [x[:-1] for x in lines2]
f.close()

seeds = [int(x) for x in lines[0].split(" ")[1:]]
lines = lines[3:]
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
    ranges = []
    maps = {}
    soils = []
    for x in range(impor):
        vals = [int(lin) for lin in lines[x].split(" ")]
        ranges += [vals]
    ranges.sort(key=lambda x:x[0])
    for seed in seedss:
        # print(seed)
        for rang in ranges:
            if seed >= rang[0]:
                if seed < rang[0] + rang[2]:
                    maps[seed] = seed - rang[0] + rang[1]
                    soils += [seed - rang[0] + rang[1]]
                    break
            else:
                maps[seed] = seed
                soils += [seed]
                break
    return [impor, maps, soils]

print(mapping(lines, seeds))
     
# print(lines)
