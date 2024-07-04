"""NYTGames Letterboxed Solver
"""
from collections import defaultdict

# Given lists
lists = [input("Top Letters: ").strip().lower(),
            input("Right Letters: ").strip().lower(),
            input("Bottom Letters: ").strip().lower(),
            input("Left Letters: ").strip().lower()]
letterset = set(''.join(lists))
N = 3
wordlist = set()

# load valid words from dict.txt
with open('letterboxed_wordlist.txt', 'r', encoding="utf-8") as input_dict_file:
    for line in input_dict_file:
        word = line.strip().lower().replace("'", '')
        if len(word) > 3 and all(letter in letterset for letter in word):
            wordlist.add(word)

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

# filter out invalid words from wordlist
valid_words = set()
for word in wordlist:
    if is_valid_word(word, lists):
        valid_words.add(word)
wordlist = valid_words

print("Best words: ", sorted(wordlist, key=lambda x: len(set(x)), reverse=True)[:5])

# create a dictionary of starting letters
starting_letters = defaultdict(list)
for word in wordlist:
    starting_letters[word[0]].append(word)

solutions: list[tuple] = []
def find_solution(given_letterset: set, given_wordlist: set[str],
                  current_solution: str, num_words: int=0):
    """Find a solution to the letterboxed puzzle

    Args:
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

            find_solution(new_letterset, new_wordlist,
                          current_solution + given_word + "-", num_words + 1)

find_solution(letterset, wordlist, "")

# print sorted solutions
solutions.sort(key=lambda x: x[1])
solutions.sort(key=lambda x: len(x[0]))

print("Number of solutions: ", len(solutions))
print("10 shortest solutions: ", [sol[0] for sol in solutions[:10]])

# write to letterboxed_solutions.txt
with open('letterboxed_solutions.txt', 'w', encoding="utf-8") as output_file:
    output_file.write("\nNumber of solutions: " + str(len(solutions)) + "\n")
    output_file.write("10 shortest solutions: " + str([sol[0] for sol in solutions[:10]]) + "\n")
    output_file.write("10 longest solutions: " + str([sol[0] for sol in solutions[-10:]]) + "\n")
    for solution in solutions:
        output_file.write(solution[0] + "\n")

print("Remaining solutions in letterboxed_solutions.txt.")
