import numpy as np
from pathlib import Path
from collections import deque


EXPECTED_FILE_NAMES = ['walls', 'terrain']
CSV_SUFFIX = '.csv'
CSV_DIR = 'csvs'

EMPTY, DRYWALL, WOOD, STONE = [0, 1, 2, 3]
MUD, DIRT, STONE, BEDROCK = [0, 1, 2, 3]
FILLED = 8

LEAK_ORIGIN = (8, 8)
MIDDLE_OF_CIRCLE = (4, 4)

def unstable_walls(walls: np.ndarray, terrain: np.ndarray, threshold: int = MUD) -> int:

    #------------------------------------------ YOUR CODE GOES HERE ------------------------------------------
    # Question 2a
    sum = 0
    for x1, x2 in zip(walls, terrain):
        #print("walls:",x1, "terrain:", x2, end = "")
        #curr = 0
        for y1, y2 in zip(x1, x2):
            if(y1 != 0):
                if(y2 <= threshold):
                    sum += 1;
                    #curr += 1;
        #print(" unstable for this row: ", curr, "total sum: ", sum)
    return sum
    #---------------------------------------------------------------------------------------------------------
def add_adjacent_spaces(stack: deque(), walls: np.ndarray) -> int:
    (x_max, y_max) = walls.shape
    sum = 0
    (r, c) = stack.pop()
    walls[(r, c)] = FILLED
    #fill in: NORTH, EAST, SOUTH, WEST adjacent spots
    if(r+1 < x_max and walls[(r+1, c)] == EMPTY):
        walls[(r+1, c)] = FILLED
        stack.append((r+1, c))
        sum += 1
    if(r-1 >= 0 and walls[(r-1, c)] == EMPTY):
        walls[(r-1, c)] = FILLED
        stack.append((r-1, c))
        sum += 1
    if(c+1 < y_max and walls[(r, c+1)] == EMPTY):
        walls[(r, c+1)] = FILLED
        stack.append((r, c+1))
        sum += 1
    if(c-1 >= 0 and walls[(r, c-1)] == EMPTY):
        walls[(r, c-1)] = FILLED
        stack.append((r, c-1))
        sum += 1
    return sum

#replaced_with is a helper method that replaces a certain value in a given 2d array with a new value, 
#then returns the number of elements changed
def replace_with(walls: np.ndarray, to_replace: int, replacement: int) -> int:
    i, j = walls.shape
    sum = 0
    for x in range(i):
        for y in range(j):
            if(walls[(x, y)] == to_replace):
                walls[(x, y)] = replacement
                sum += 1
    return sum

def leak_territory(walls: np.ndarray, leak_origin: tuple[int] = LEAK_ORIGIN) -> int:

    #------------------------------------------ YOUR CODE GOES HERE ------------------------------------------
    # Question 2b
    (x_max, y_max) = walls.shape
    #print("xmax = ", x_max, "Y max = ", y_max)
    #start of sum is 1 for the LEAK_ORIGIN
    sum = 1
    stack = deque()
    #leaks should only happen where there is not a wall
    if(walls[(leak_origin)] != EMPTY):
        return 0
    stack.append(leak_origin)
    #print(" part 1 this is contents of ur stack: ",stack)

    while(len(stack) > 0):
        sum += add_adjacent_spaces(stack, walls)
        #print("this is contents of ur stack: ",stack)

    #(r, c) = LEAK_ORIGIN
    #To show the filled area
    #for x1 in walls:
    #    print("walls:",x1)

    #unfill the area
    replace_with(walls, FILLED, EMPTY);

    #print("double check the unfill:")
    #for x1 in walls:
    #    print("walls:",x1)
    return sum
    #---------------------------------------------------------------------------------------------------------

def validate_env(csv_dir: Path):
    
    if (not csv_dir.exists()):
        raise('csv dir does not exist')
    for expected_file in EXPECTED_FILE_NAMES:
        expected_file_path = csv_dir / (expected_file + CSV_SUFFIX)
        if (not expected_file_path.exists()):
            raise(f'{expected_file_path} does not exist')

def main():

    parent_dir = Path(__file__).parent.resolve()
    csv_dir = parent_dir / CSV_DIR
    validate_env(csv_dir)

    WALLS = np.loadtxt(CSV_DIR / Path('walls.csv'), delimiter=',').astype(np.int8)
    TERRAIN = np.loadtxt(CSV_DIR / Path('terrain.csv'), delimiter=',').astype(np.int8)
    TERRAIN_MUD = np.loadtxt(CSV_DIR / Path('terrain_mud.csv'), delimiter=',').astype(np.int8)

    WALLS_GONE_TEST = np.loadtxt(CSV_DIR / Path('wall_test.csv'), delimiter=',').astype(np.int8)
    WALLS_IN_CIRCLE_TEST = np.loadtxt(CSV_DIR / Path('walls_test2.csv'), delimiter=',').astype(np.int8)

    # Q2a result printed here
    print('unstable_walls:', unstable_walls(np.copy(WALLS), np.copy(TERRAIN), threshold=DIRT))

    #Testing Q2a
    print('unstable_walls, expected output of : 0, actual output of : ', unstable_walls(np.copy(WALLS_GONE_TEST), np.copy(TERRAIN), threshold = DIRT))

    #Testing Q2a
    print('unstable_walls, expected output of : 12, actual output of : ', unstable_walls(np.copy(WALLS_IN_CIRCLE_TEST), np.copy(TERRAIN_MUD), threshold = DIRT))

    #Testing Q2a
    print('unstable_walls, expected output of : 12, actual output of : ', unstable_walls(np.copy(WALLS_IN_CIRCLE_TEST), np.copy(TERRAIN_MUD)))

    #Testing Q2a
    print('unstable_walls, expected output of : 7, actual output of : ', unstable_walls(np.copy(WALLS_IN_CIRCLE_TEST), np.copy(TERRAIN), threshold = DIRT))




    # Q2b result printed here
    print('leak_territory:', leak_territory(np.copy(WALLS), leak_origin=LEAK_ORIGIN))

    #Testing Q2b
    print('leak_territory_test1, expected output of : 100, actual output of :', leak_territory(np.copy(WALLS_GONE_TEST), leak_origin=LEAK_ORIGIN))

    #Testing Q2b
    print('leak_territory_test2, expected output of : 9, actual output of : ', leak_territory(np.copy(WALLS_IN_CIRCLE_TEST), leak_origin=MIDDLE_OF_CIRCLE))
    
    #Testing Q2b
    print('leak_territory_test2, expected output of : 79, actual output of : ', leak_territory(np.copy(WALLS_IN_CIRCLE_TEST), leak_origin=LEAK_ORIGIN))


if __name__ == '__main__':
    main()
