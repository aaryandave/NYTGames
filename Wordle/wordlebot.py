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
with open('./wordle_wordlist.txt', 'r', encoding="utf-8") as input_dict_file:
    words = [line.strip().lower().replace("'", '') for line in input_dict_file]

def is_valid_word(word_to_check: str) -> bool:
    """Check if a word is a valid Wordle guess.

    Args:
        word_to_check (str): The word to check

    Returns:
        bool: True if the word is valid, False otherwise
    """
    if len(word_to_check) != 5:
        return False
    if any(letter in word_to_check for letter in GRAY_LETTERS):
        return False
    if not all(letter in GREEN_LETTERS[i] for i, letter in enumerate(word_to_check)):
        return False
    for letter, indices in YELLOW_LETTERS.items():
        if letter not in word_to_check:
            return False
        if letter in word_to_check and any(word_to_check[ind] == letter for ind in indices):
            return False
    return True

# filter valid words
valid_words = [word for word in words if is_valid_word(word)]

# sort by number of unique letters
valid_words.sort(reverse=True, key=lambda x: len(set(x)))

# print and write results
num_solutions = len(valid_words)
best_solutions = valid_words[:5]

print("Number of words:", num_solutions)
print("Best 5 words:", best_solutions)

with open('wordle_solutions.txt', 'w', encoding="utf-8") as output_file:
    output_file.write(f"Number of possible solutions: {num_solutions}\n")
    output_file.write(f"Best 5 solutions: {best_solutions}\n")
    for word in valid_words:
        output_file.write(word + "\n")

print("Remaining solutions in wordle_wordlist.txt.")
