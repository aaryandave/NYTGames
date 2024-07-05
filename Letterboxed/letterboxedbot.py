"""NYTGames Letterboxed Solver
"""
from collections import defaultdict

N = 3

def get_lists() -> list[str]:
    """Get the character lists from the user.

    Returns:
        list[str]: The character lists
    """
    return [input("Top Letters: ").strip().lower(),
            input("Right Letters: ").strip().lower(),
            input("Bottom Letters: ").strip().lower(),
            input("Left Letters: ").strip().lower()]

def get_worldset_from_file(file_path: str, letterset: set[str]) -> set[str]:
    """Read words from a file.

    Args:
        file_path (str): The path to the file
        letterset (set[str]): The set of letters

    Returns:
        set[str]: A set of words
    """
    with open(file_path, 'r', encoding="utf-8") as input_dict_file:
        wordset = set()
        for line in input_dict_file:
            word = line.strip().lower().replace("'", '')
            if len(word) > 3 and all(letter in letterset for letter in word):
                wordset.add(word)

    return wordset

def is_valid_word(word_to_check: str, character_lists: list[str]) -> bool:
    """Check if a word is valid given the character lists

    Args:
        word_to_check (str): The word to check
        character_lists (list[str]): The character lists of each side

    Returns:
        bool: True if the word is valid, False otherwise
    """
    prev_idx = None
    for c in word_to_check:
        for idx, lst in enumerate(character_lists):
            if c in lst:
                if prev_idx == idx:
                    return False
                prev_idx = idx
    return True

def get_starting_letters(wordlist: set[str]) -> dict[str, list[str]]:
    """Get the starting letters of the words

    Args:
        wordlist (set[str]): The set of words

    Returns:
        dict[str, list[str]]: The dictionary of starting letters
    """
    starting_letters = defaultdict(list)
    for word in wordlist:
        starting_letters[word[0]].append(word)
    return starting_letters

def find_solution(solutions: list[tuple], starting_letters: dict[str, list[str]],
                  given_letterset: set, given_wordlist: set[str], current_solution: str,
                  num_words: int=0):
    """Find a solution to the letterboxed puzzle

    Args:
        solutions (list[tuple]): The list of solutions
        starting_letters (dict[str, list[str]]): The dictionary of starting letters
        given_letterset (set): The set of letters
        given_wordlist (set[str]): The set of words
        current_solution (str): The current solution
        num_words (int, optional): The number of words. Defaults to 0.
    """
    if num_words > N:
        return
    if not given_letterset:
        solutions.append((current_solution[:-1], num_words))
        return
    for given_word in given_wordlist:
        if current_solution == "" or given_word[0] == current_solution[-2]:
            new_letterset = given_letterset - set(given_word)

            new_wordlist = set(starting_letters[given_word[-1]])
            if given_word in new_wordlist:
                new_wordlist.remove(given_word)

            find_solution(solutions, starting_letters, new_letterset, new_wordlist,
                          current_solution + given_word + "-", num_words + 1)

def write_solutions(solutions: list[tuple], file_path: str='letterboxed_solutions.txt') -> None:
    """Write the solutions to a file.

    Args:
        solutions (list[tuple]): The list of solutions
        file_path (str, optional): The path to the file. Defaults to 'letterboxed_solutions.txt'.
    """
    with open(file_path, 'w', encoding="utf-8") as output_file:
        output_file.write(f"Number of solutions: {len(solutions)}\n")
        output_file.write(f"10 shortest solutions: {[sol[0] for sol in solutions[:10]]}\n")
        output_file.write(f"10 longest solutions: {[sol[0] for sol in solutions[-10:]]}\n")
        for solution in solutions:
            output_file.write(solution[0] + "\n")

def main():
    """Main function.
    """
    lists = get_lists()
    letterset = set(''.join(lists))

    wordset = get_worldset_from_file('letterboxed_wordlist.txt', letterset)
    wordlist = [word for word in wordset if is_valid_word(word, lists)]

    print("Best starting words: ", sorted(wordlist, key=lambda x: len(set(x)), reverse=True)[:5])

    solutions = []
    find_solution(solutions, get_starting_letters(wordlist), letterset, wordlist, "")

    solutions.sort(key=lambda x: x[1])
    solutions.sort(key=lambda x: len(x[0]))

    print("Number of solutions: ", len(solutions))
    print("10 shortest solutions: ", [sol[0] for sol in solutions[:10]])

    write_solutions(solutions)

    print("Remaining solutions in letterboxed_solutions.txt.")

if __name__ == "__main__":
    main()
