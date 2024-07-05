"""NYTGames Spelling Bee Solver
"""

def get_inputs() -> tuple[str, set[str]]:
    """Get the center letter and remaining letters from the user.

    Returns:
        tuple[str, set[str]]: The center letter and remaining letters
    """
    center_letter = input("Center letter: ")
    remaining_letters = set(input("Remaining letters: "))
    remaining_letters.add(center_letter)
    return center_letter, remaining_letters

def read_words(file_path: str) -> set[str]:
    """Read words from a file.

    Args:
        file_path (str): The path to the file

    Returns:
        set[str]: A set of words
    """
    with open(file_path, 'r', encoding="utf-8") as input_dict_file:
        return {line.strip().lower().replace("'", '') for line in input_dict_file}

def is_valid_word(word_to_check: str, center_letter: str, remaining_letters: set[str]) -> bool:
    """Check if a word is a valid Spelling Bee word.

    Args:
        word_to_check (str): The word to check
        center_letter (str): The center letter
        remaining_letters (set[str]): The remaining letters

    Returns:
        bool: True if the word is valid, False otherwise
    """
    # Check if the word contains the center letter
    if center_letter not in word_to_check:
        return False

    # Check if the word contains only the remaining letters
    if not all(letter in remaining_letters for letter in word_to_check):
        return False

    # Check if the word is at least 4 letters long
    if len(word_to_check) < 4:
        return False

    return True

def write_solutions(valid_words: set[str], file_path: str='spellingbee_solutions.txt') -> None:
    """Write the solutions to a file.

    Args:
        valid_words (set[str]): The set of valid words
        file_path (str, optional): The path to the file. Defaults to 'spellingbee_solutions.txt'.
    """
    with open(file_path, 'w', encoding="utf-8") as output_file:
        output_file.write(f"Num Words: {len(valid_words)}\n")
        for word in valid_words:
            output_file.write(word + "\n")

def main():
    """Main function.
    """
    center_letter, remaining_letters = get_inputs()
    word_list = read_words('SpeelingBee/wordlist.txt')

    valid_words = {word for word in word_list if
                   is_valid_word(word, center_letter, remaining_letters)}
    valid_words_list = sorted(valid_words, key=len, reverse=True)
    print(f'Num Words: {len(valid_words)}')
    print("Longest words: ", valid_words_list[:5])

    write_solutions(valid_words)
    print("Remaining solutions in spellingbee_solutions.txt.")

if __name__ == '__main__':
    main()
