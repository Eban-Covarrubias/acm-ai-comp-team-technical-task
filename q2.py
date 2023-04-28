import numpy as np
from pathlib import Path

EXPECTED_FILE_NAMES = ['walls', 'terrain']
CSV_SUFFIX = '.csv'
CSV_DIR = 'csvs'

EMPTY, DRYWALL, WOOD, STONE = [0, 1, 2, 3]
MUD, DIRT, STONE, BEDROCK = [0, 1, 2, 3]

LEAK_ORIGIN = (6, 5)

def unstable_walls(walls: np.ndarray, terrain: np.ndarray, threshold: int = MUD) -> int:

    #------------------------------------------ YOUR CODE GOES HERE ------------------------------------------
    # Question 2a
    sum = 0
    for x in walls:
        for y in x:
            if(y != EMPTY):
                if(terrain[x][y] == MUD or terrain[x][y] == DIRT):
                    sum += 1
    return sum
    #---------------------------------------------------------------------------------------------------------

def leak_territory(walls: np.ndarray, leak_origin: tuple[int] = LEAK_ORIGIN) -> int:

    #------------------------------------------ YOUR CODE GOES HERE ------------------------------------------
    # Question 2b
    
    return -1
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

    # Q2a result printed here
    print('unstable_walls:', unstable_walls(np.copy(WALLS), np.copy(TERRAIN), threshold=DIRT))

    # Q2b result printed here
    print('leak_territory:', leak_territory(np.copy(WALLS), leak_origin=LEAK_ORIGIN))

if __name__ == '__main__':
    main()
