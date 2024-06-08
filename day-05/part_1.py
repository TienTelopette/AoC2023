import os

path = os.path.join(os.getcwd(), "day-05", "input.txt")
file = open(path)
data = file.read()

def get_destination(source, map):
    # Takes source number and converts to destination following the given map's indications
    for m in map:
        split = m.split(" ")
        destination_start = int(split[0])
        source_start = int(split[1])
        rng = int(split[2])
        
        if source in range(source_start, source_start + rng):
            offset = destination_start - source_start
            return source + offset
    return source
    

split = data.split("\n\n")
seeds = split[0].split(": ")[1].split(" ")
seed_to_soil = split[1].split(":\n")[1].split("\n")
soil_to_fertilizer = split[2].split(":\n")[1].split("\n")
fertilizer_to_water = split[3].split(":\n")[1].split("\n")
water_to_light = split[4].split(":\n")[1].split("\n")
light_to_temperature = split[5].split(":\n")[1].split("\n")
temperature_to_humidity = split[6].split(":\n")[1].split("\n")
humidity_to_location = split[7].split(":\n")[1].split("\n")

ordered_maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

lowest_location_number = 99999999999999999999

for seed in seeds:
    source = int(seed)
    for map in ordered_maps:
        source = get_destination(source, map)
    if lowest_location_number > source:
        lowest_location_number = source
print(lowest_location_number)