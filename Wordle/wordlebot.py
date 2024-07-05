"""NYTGames Wordle Solver
"""
# input gray letters as a string
GRAY_LETTERS = ''

# input green letters into the corresponding index
GREEN_LETTERS = {0: "", 1: "", 2: "", 3: "", 4: ""}

# input yellow letters as a dictionary of all the yellow indices, like this:
# {'a': [0, 1, 2], 'b': [3, 4]}
YELLOW_LETTERS: dict[str, list[int]] = {}

# load wordlist from file
def read_words(file_path: str) -> list[str]:
    """Read words from a file.

    Args:
        file_path (str): The path to the file

    Returns:
        list[str]: A list of words
    """
    with open(file_path, 'r', encoding="utf-8") as input_dict_file:
        return [line.strip().lower().replace("'", '') for line in input_dict_file]

def is_valid_word(word_to_check: str) -> bool:
    """Check if a word is a valid Wordle guess.

    Args:
        word_to_check (str): The word to check

    Returns:
        bool: True if the word is valid, False otherwise
    """
    # Check if the word is 5 letters long
    if len(word_to_check) != 5:
        return False

    # Check if the word contains any gray letters
    if any(letter in word_to_check for letter in GRAY_LETTERS):
        return False

    # Check if the word contains all green letters
    if not all(GREEN_LETTERS[i] == letter for i, letter in enumerate(word_to_check)):
        return False

    # Check if the word contains any yellow letters
    for letter, indices in YELLOW_LETTERS.items():
        if letter not in word_to_check:
            return False
        if letter in word_to_check and any(word_to_check[ind] == letter for ind in indices):
            return False

    return True

def save_results(valid_words: list[str], num_solutions: int, best_solutions: list[str],
                 file_path: str='wordle_solutions.txt'):
    """Save the results to a file.

    Args:
        valid_words (list[str]): The list of valid words
        num_solutions (int): The number of solutions
        best_solutions (list[str]): The best 5 solutions
        file_path (str, optional): The path to the output file. Defaults to 'wordle_solutions.txt'.
    """
    with open(file_path, 'w', encoding="utf-8") as output_file:
        output_file.write(f"Number of possible solutions: {num_solutions}\n")
        output_file.write(f"Best 5 solutions: {best_solutions}\n")
        for word in valid_words:
            output_file.write(word + "\n")

print("Remaining solutions in wordle_wordlist.txt.")

def main():
    """Main function to solve Wordle.
    """
    file_words = read_words('wordle_wordlist.txt')

    valid_words = [word for word in file_words if is_valid_word(word)]
    valid_words.sort(reverse=True, key=lambda x: len(set(x)))

    num_solutions = len(valid_words)
    best_solutions = valid_words[:5]

    print("Number of words:", num_solutions)
    print("Best 5 words:", best_solutions)

    save_results(valid_words, num_solutions, best_solutions)

if __name__ == "__main__":
    main()
