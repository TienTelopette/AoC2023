import re

file = open("/Users/Tien/Documents/GitHub/AoC2023/Day_5/input.txt","r")
data = file.read()

def get_destinations(source, map):
    # Takes source numbers (startindex, range) and converts to list of destination tuples (startindex, range)
    # following the given map's indications
    map.sort(key = lambda x: x[1])
    result = []
    entering_source = [source]
    while entering_source:
        seed = entering_source.pop()
        for m in map:
            seed_start = int(seed[0])
            seed_end = seed_start + int(seed[1]) - 1

            rng = int(m[2])
            destination_start = int(m[0])
            source_start = int(m[1])
            source_end = int(source_start) + rng - 1
            offset = destination_start - source_start
        

            intersect_start = max(seed_start, source_start)
            intersect_end =  min(seed_end, source_end)

            if intersect_start > intersect_end:
                # no intersections
                if seed_end < source_start or map.index(m) == len(map) - 1:
                    # last loop with no intersections or seed range is already lower than source start in map
                    result.append(seed)
                    break
                continue
            else:
                new_seed = (intersect_start + offset, intersect_end - intersect_start + 1) # convert whole intersection range to new seed
                result.append(new_seed)
                if seed_start >= source_start and seed_end <= source_end:
                    # all seed range processed
                    break
                
                if seed_start < intersect_start:
                    # -- ---      managing head of seeds range -> add to result
                    #    -------
                    result.append((seed_start, intersect_start - seed_start + 1)) 
                if seed_end > intersect_end:
                    #    ---- --- managing tail of the seeds range -> to be processed with next maps
                    # -------     or to be added to result if it's the last map
                    if map.index(m) == len(map) - 1:
                        result.append((intersect_end + 1, seed_end - (intersect_end + 1) + 1))
                        break
                    seed = (intersect_end + 1, seed_end - (intersect_end + 1) + 1)
                else:
                    # no tail chunks to be processed any further
                    break
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

ordered_maps = [seed_to_soil, soil_to_fertilizer,
                fertilizer_to_water, water_to_light,
                light_to_temperature, temperature_to_humidity,
                humidity_to_location]


lowest_location_number = float("inf")

light_to_temperature.sort(key = lambda x: x[1])

seeds.sort()
converted_seeds = []
for map in ordered_maps:
    converted_seeds.clear()
    while seeds:
        seed = seeds.pop(-1)
        converted_seeds.extend([x for x in get_destinations(seed, map) if x not in converted_seeds])
    seeds = sorted(converted_seeds)

lowest_location_number = sorted(converted_seeds)[0]
print(lowest_location_number)