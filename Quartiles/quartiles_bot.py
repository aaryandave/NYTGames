"""NYTGames Quartiles Solver
"""

def get_tile_set() -> set[str]:
    """Get the tile set from the user.

    Returns:
        set[str]: The tile set
    """
    return set(input("Enter the tile set space separated: ").split())

def read_words(file_path: str) -> set[str]:
    """Read words from a file.

    Args:
        file_path (str): The path to the file

    Returns:
        set[str]: A set of words
    """
    with open(file_path, 'r', encoding="utf-8") as input_dict_file:
        return {line.strip().lower().replace("'", '') for line in input_dict_file}

def get_solution(tile_set: set[str], wordlist: set[str]) -> set[str]:
    """Get the solutions for the tile set.

    Args:
        tile_set (set[str]): The tile set
        wordlist (set[str]): The list of words

    Returns:
        set[str]: The set of solutions
    """
    results = set()

    for tile1 in tile_set:
        word = tile1
        if word in wordlist:
            results.add(word)

        for tile2 in tile_set:
            if tile1 == tile2:
                continue

            word = tile1 + tile2
            if word in wordlist:
                results.add(word)

            for tile3 in tile_set:
                if tile1 == tile3 or tile2 == tile3:
                    continue

                word = tile1 + tile2 + tile3
                if word in wordlist:
                    results.add(word)

                for tile4 in tile_set:
                    if tile1 == tile4 or tile2 == tile4 or tile3 == tile4:
                        continue

                    word = tile1 + tile2 + tile3 + tile4
                    if word in wordlist:
                        results.add(word)

    return results

def main():
    """Main function.
    """
    tile_set = get_tile_set()
    word_list = read_words('wordlist.txt')

    results = get_solution(tile_set, word_list)
    list_results = list(results)
    list_results = sorted(list_results, key=len, reverse=True)
    print(list_results)

if __name__ == '__main__':
    main()
