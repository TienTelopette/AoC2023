file = open("C:/Users/ttche/Desktop/AoC2023/Day_5/test_input.txt","r")
data = file.read()

def get_converted_seeds(seed, map):
    seeds = [seed]
    while seeds:
        for m in map:
            break


    return 0


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

for m in ordered_maps:
    m.sort(key = lambda x: x[1])


converted_seeds = []
for map in ordered_maps:
    print(map)
    while seeds:
        seed = seeds.pop(-1)
        converted_seeds = get_converted_seeds(seed, map)