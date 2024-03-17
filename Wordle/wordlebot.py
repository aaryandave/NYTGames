# input gray letters as a string
gray_letters = ''

# input green letters into the corresponding index
green_letters = {0: "", 1: "", 2: "", 3: "", 4: ""}

# input yellow letters as a dictionary of all the yellow indices, like this: 
# {'a': [0, 1, 2], 'b': [3, 4]}
yellow_letters = {}

# load wordlist from file
with open('./wordle_wordlist.txt', 'r') as input_dict_file:
    words = [line.strip().lower().replace("'", '') for line in input_dict_file]

def is_valid_word(word):
    if len(word) != 5:
        return False
    if any(letter in word for letter in gray_letters):
        return False
    if not all(green_letters[i] == "" or word[i] == green_letters[i] for i in green_letters):
        return False
    for letter, indices in yellow_letters.items():
        if letter not in word:
            return False
        if letter in word and any(word[ind] == letter for ind in indices):
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

with open('wordle_solutions.txt', 'w') as output_file:
    output_file.write("Number of possible solutions: {}\n".format(num_solutions))
    output_file.write("Best 5 solutions: {}\n".format(best_solutions))
    for word in valid_words:
        output_file.write(word + "\n")

print("Remaining solutions in wordle_wordlist.txt.")