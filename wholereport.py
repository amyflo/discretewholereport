import numpy as np
import random

# can replace colors with RGB values later
COLORS = ['red', 'pink', 'lightblue',
          'white', 'black', 'blue',
          'green', 'yellow', 'none']
MAXIMUM_SQ = 6
GRID_ROWS = 2
NUM_TRIALS = 150
WINDOW_SIZE = (1440, 1080)


def calculate_location(size, i):
    """
    Calculate the middle of each box in the grid.
    """
    return int(i * size + size // 2)


def rand_location(loc, color):
    if color == 'none':
        return loc
    width = WINDOW_SIZE[0]
    height = WINDOW_SIZE[1]

    cols = MAXIMUM_SQ // GRID_ROWS
    area_height = height / cols
    area_width = width / GRID_ROWS
    return find_loc(area_height, area_width, loc)


def find_loc(area_height, area_width, loc):
    y_bound = area_height / 4
    x_bound = area_width / 4

    x = loc[0]
    y = loc[1]
    loc_x = np.random.randint(x - x_bound, x + x_bound)
    loc_y = np.random.randint(y - y_bound, y + x_bound)
    return loc_x, loc_y


def window_locations():
    """
    Ensure that the MAXIMUM_SQ you have is divisible
    by GRID_ROWS. Returns an array of locations.
    """
    width = WINDOW_SIZE[0]
    height = WINDOW_SIZE[1]

    cols = MAXIMUM_SQ // GRID_ROWS
    area_height = height / cols
    area_width = width / GRID_ROWS

    locations = []
    for i in range(GRID_ROWS):
        for j in range(cols):
            x = calculate_location(area_width, i)
            y = calculate_location(area_height, j)
            locations.append((x, y))
    return locations


def random_block():
    """
    Creates a random block of NUM_TRIALS size;
    returns a dict of randomized trials in the block.
    """
    block = {}
    for i in range(NUM_TRIALS):
        name = 'trial' + str(i + 1)
        block[name] = random_trial()
    return block


def random_trial():
    """
    Create a randomized trial that has x number of squares
    between MIMIMUM_SQ and MAXIMUM_SQ. Returns a dict
    of tuples of the square color and number corresponding
    to a location on a grid of MAXIMUM_SQ size.
    """

    # creating randomized colors for each square
    rand_colors = np.random.randint(len(COLORS), size=MAXIMUM_SQ)
    random.shuffle(COLORS)
    colors = [COLORS[num] for num in rand_colors]

    # shuffles potential locations
    locations = window_locations()
    random.shuffle(locations)

    # color, coordinate for each trial
    trial = {}
    for i in range(MAXIMUM_SQ):
        name = 'square' + str(i + 1)
        trial[name] = {}
        square = trial[name]
        square['location'] = rand_location(locations[i], colors[i])
        square['color'] = colors[i]
    return trial


def main():
    """
    Print out blocks.
    """
    trial = random_block()
    for key, value in trial.items():
        print(key.upper())

        for key2, value2 in value.items():
            print(key2, value2)
        print()


if __name__ == "__main__":
    main()