width = int(raw_input("Input width of floor in inches: "))
height = int(raw_input("input height of floor in inches: "))
cost_of_tile = int(raw_input("Input cost of  a single tile in USD: "))
area_of_floor = height * width

area_of_tile = 144

no_of_tiles = area_of_floor/area_of_tile

total_cost_tiles = cost_of_tile*no_of_tiles

print('Total cost is {0}').format(total_cost_tiles)