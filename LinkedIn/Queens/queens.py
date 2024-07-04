"""LinkedIn Queens Puzzle Solver
"""
import math
from time import perf_counter

QUEEN_CHAR: str = '&'
STAR_CHAR: str = '*'

def read_puzzle(filepath: str) -> str:
    """Reads a puzzle from a file

    Args:
        filepath (str): The path to the file

    Returns:
        str: The puzzle
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read().replace('\n', '')

def print_puzzle(puzzle: str) -> None:
    """Prints the puzzle

    Args:
        puzzle (str): The puzzle to print
    """
    side_len: int = int(math.sqrt(len(puzzle)))
    for i in range(side_len):
        print(puzzle[i*side_len:(i+1)*side_len])

def place_queen(puzzle: str, index: int) -> str:
    """Places a queen on the puzzle at the given index and blocks the squares

    Args:
        puzzle (str): The puzzle
        index (int): The index to place the queen

    Returns:
        str: The puzzle with the queen placed and the squares blocked
    """
    side_len: int = int(math.sqrt(len(puzzle)))
    row: int = index // side_len
    col: int = index % side_len

    child_puzzle: str = puzzle

    for i in range(side_len):
        child_puzzle = child_puzzle[:row*side_len+i] + STAR_CHAR + child_puzzle[row*side_len+i+1:]
        child_puzzle = child_puzzle[:i*side_len+col] + STAR_CHAR + child_puzzle[i*side_len+col+1:]

    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            if row+i >= 0 and row+i < side_len and col+j >= 0 and col+j < side_len:
                child_puzzle = child_puzzle[:(row+i)*side_len+col+j] + STAR_CHAR + child_puzzle[
                    (row+i)*side_len+col+j+1:]

    child_puzzle = child_puzzle.replace(puzzle[index], STAR_CHAR)

    child_puzzle = child_puzzle[:index] + QUEEN_CHAR + child_puzzle[index+1:]

    return child_puzzle

def get_all_moves(puzzle: str) -> list[tuple]:
    """Get all possible moves for the puzzle

    Args:
        puzzle (str): The puzzle

    Returns:
        list[tuple]: A list of tuples containing the index and the number of times the character 
        appears
    """
    moves: list[tuple] = []
    for i, char in enumerate(puzzle):
        if char != STAR_CHAR and char != QUEEN_CHAR:
            moves.append((i, puzzle.count(char)))

    return sorted(moves, key=lambda x: x[1])

def solve_puzzle(puzzle: str) -> str:
    """Solves the puzzle

    Args:
        puzzle (str): The puzzle

    Returns:
        str: The solved puzzle
    """
    stack: list[str] = [puzzle]
    side_len: int = int(math.sqrt(len(puzzle)))
    while stack:
        current_puzzle: str = stack.pop()
        if current_puzzle.count(QUEEN_CHAR) == side_len:
            return current_puzzle
        moves: list[tuple] = get_all_moves(current_puzzle)
        for move in moves:
            stack.append(place_queen(current_puzzle, move[0]))
    return ''

def print_coords(solution: str) -> None:
    """Prints the coordinates of the queens

    Args:
        solution (str): The solved puzzle
    """
    side_len: int = int(math.sqrt(len(solution)))
    queen_indeces: list[int] = [i for i, char in enumerate(solution) if char == QUEEN_CHAR]
    for index in queen_indeces:
        row: int = index // side_len + 1
        col: int = index % side_len + 1
        print(f'Queen {row}: ({row=}, {col=})')

def main():
    """Main function
    """
    puzzle = read_puzzle('linkedin/queens/puzzle.txt')

    print_puzzle(puzzle)
    print()

    puzzle_start = perf_counter()
    solution = solve_puzzle(puzzle)
    puzzle_end = perf_counter()
    print_puzzle(solution)
    print()

    print_coords(solution)
    print(f"Time to solve: {puzzle_end - puzzle_start:.6f} seconds")

if __name__ == '__main__':
    main()
