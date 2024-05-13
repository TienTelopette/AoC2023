import re

file = open("C:/Users/ttche/Desktop/AoC2023/Day_5/test_input.txt","r")
data = file.read()

def get_destinations(source, map):
    # Takes source numbers (startindex, range) and converts to list of destination tuples (startindex, range)
    # following the given map's indications
    map.sort(key = lambda x: x[1])
    result = []
    # print("SOURCONE: ", source)
    entering_source = [source]
    found = False
    while entering_source:
        # print("\nCIAO")
        print("Entering a loop with: ", entering_source)
        seed = entering_source.pop()
        found = False
        for m in map:
            print("----\nwith map: ", m)
            print(map.index(m) + 1, " of ", len(map))
            rng = int(m[2])
            destination_start = int(m[0])
            source_start = int(m[1])
            source_end = int(source_start) + rng
            offset = destination_start - source_start
            seed_start = int(seed[0])
            seed_end = seed_start + int(seed[1])
            seed_rng = seed[1]

            intersect_start = max(seed_start, source_start)
            intersect_end =  min(seed_end, source_end)
            # print("seed: ", seed)
            # print("seed_end: ", seed_end)
            # print("intersection result: ", intersect_start, " - ", intersect_end)
            # print("seed_start: ", seed_start, " intersection_start: ", intersect_start)
            # print("source_start: ", source_start)
            # print("source_end: ", source_end)
            
            if intersect_start > intersect_end:
                # last loop with no intersections or seed range is already lower than source start in map
                if seed_end < source_start or map.index(m) == len(map) - 1:
                    if seed not in result:
                        print("added seed ", seed, " for being lower than startindex")
                        result.append(seed)
                    break
                # no intersections
                # print("no intersections")
                continue
            else:
                found = True
                # print("intersection found")
                new_seed = (intersect_start + offset, intersect_end - intersect_start)
                print("from seed: ", seed)
                print("new_seed: ", intersect_start + offset, intersect_end - intersect_start + 1, " offset: ", offset)
                if new_seed not in result:
                    result.append(new_seed)
                if seed_start < intersect_start:
                    # print("BOH")
                    # -----
                    #   -------
                    if (seed_start, intersect_start - seed_start) not in result:
                        print("add to result: ", (seed_start, intersect_start - seed_start))
                        result.append((seed_start, intersect_start - seed_start)) 
                if seed_end > intersect_end:
                    #    -------
                    # -------
                    # print("ayo")
                    print("readded to seeds: ", intersect_end + 1, seed_end - intersect_end)
                    if map.index(m) == len(map) - 1:
                        result.append((intersect_end + 1, seed_end - intersect_end))
                        break
                    entering_source.append((intersect_end + 1, seed_end - intersect_end))
        if not found:
            if seed not in result:
                result.append(seed)
    # print("niente: ", result)
    return result

split = data.split("\n\n")
seeds = split[0].split(": ")[1].split(" ")
seeds = [(int(seeds[i]), int(seeds[i+1])) for i in range(0, len(seeds), 2)] # List of Tuples (start_index, range)
seed_to_soil = split[1].split(":\n")[1].split("\n")
seed_to_soil = [(int(seed_to_soil[i].split(" ")[0]), int(seed_to_soil[i].split(" ")[1]), int(seed_to_soil[i].split(" ")[2])) for i in range(len(seed_to_soil))]
soil_to_fertilizer = split[2].split(":\n")[1].split("\n")
soil_to_fertilizer = [(int(soil_to_fertilizer[i].split(" ")[0]), int(soil_to_fertilizer[i].split(" ")[1]), int(soil_to_fertilizer[i].split(" ")[2])) for i in range(len(soil_to_fertilizer))]
fertilizer_to_water = split[3].split(":\n")[1].split("\n")
fertilizer_to_water = [(int(fertilizer_to_water[i].split(" ")[0]), int(fertilizer_to_water[i].split(" ")[1]), int(fertilizer_to_water[i].split(" ")[2])) for i in range(len(fertilizer_to_water))]
water_to_light = split[4].split(":\n")[1].split("\n")
water_to_light = [(int(water_to_light[i].split(" ")[0]), int(water_to_light[i].split(" ")[1]), int(water_to_light[i].split(" ")[2])) for i in range(len(water_to_light))]
light_to_temperature = split[5].split(":\n")[1].split("\n")
light_to_temperature = [(int(light_to_temperature[i].split(" ")[0]), int(light_to_temperature[i].split(" ")[1]), int(light_to_temperature[i].split(" ")[2])) for i in range(len(light_to_temperature))]
temperature_to_humidity = split[6].split(":\n")[1].split("\n")
temperature_to_humidity = [(int(temperature_to_humidity[i].split(" ")[0]), int(temperature_to_humidity[i].split(" ")[1]), int(temperature_to_humidity[i].split(" ")[2])) for i in range(len(temperature_to_humidity))]
humidity_to_location = split[7].split(":\n")[1].split("\n")
humidity_to_location = [(int(humidity_to_location[i].split(" ")[0]), int(humidity_to_location[i].split(" ")[1]), int(humidity_to_location[i].split(" ")[2])) for i in range(len(humidity_to_location))]
ordered_maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]


lowest_location_number = 99999999999999999999

seeds.sort()
# print("seeds initially: ", seeds)
converted_seeds = []
for map in ordered_maps:
    # print("for map number: ", ordered_maps.index(map) + 1)
    converted_seeds = []
    while seeds:
        seed = seeds.pop(-1)
        # print("entering seed: ", seed)
        converted_seeds.extend([x for x in get_destinations(seed, map) if x not in converted_seeds])
        # print("converted: ", converted_seeds)
        # print(sorted(source))
    seeds = sorted(converted_seeds)
    print("after conversion ", ordered_maps.index(map) + 1, ": ", seeds, "\n")

    # print("AIA ", converted_seeds)

lowest_location_number = sorted(converted_seeds)[0]
print(lowest_location_number)