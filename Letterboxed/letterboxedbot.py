from collections import defaultdict

# Given lists
lists = ['nui', 'sco', 'rat', 'jhd']
letterset = set(''.join(lists))
n = 2
wordlist = set()

# Load valid words from dict.txt
with open('letterboxed_wordlist.txt', 'r') as input_dict_file:
    for line in input_dict_file:
        word = line.strip().lower().replace("'", '')
        if len(word) > 3 and all(letter in letterset for letter in word):
            wordlist.add(word)

# Function to check if a word is valid
def is_valid_word(word, lists):
    prev_idx = None
    for i, c in enumerate(word):
        for idx, lst in enumerate(lists):
            if c in lst:
                if prev_idx == idx:
                    return False
                prev_idx = idx
    return True

# Filter out invalid words from wordlist
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

solutions = []
def find_solution(letterset, wordlist, solution, num_words=0):
    if num_words > n:
        return
    if not letterset:
        solutions.append((solution[:-1], num_words))
        return
    for word in wordlist:
        if solution == "" or word[0] == solution[-2]:
            new_letterset = letterset - set(word)

            new_wordlist = starting_letters[word[-1]]
            if word in new_wordlist:
                new_wordlist.remove(word)

            find_solution(new_letterset, new_wordlist, solution + word + "-", num_words + 1)

find_solution(letterset, wordlist, "")

# print sorted solutions
solutions.sort(key=lambda x: x[1])
solutions.sort(key=lambda x: len(x[0]))

print("Number of solutions: ", len(solutions))
print("10 shortest solutions: ", [sol[0] for sol in solutions[:10]])

# write to letterboxed_solutions.txt
with open('letterboxed_solutions.txt', 'w') as output_file:
    output_file.write("\nNumber of solutions: " + str(len(solutions)) + "\n")
    output_file.write("10 shortest solutions: " + str([sol[0] for sol in solutions[:10]]) + "\n")
    output_file.write("10 longest solutions: " + str([sol[0] for sol in solutions[-10:]]) + "\n")
    for solution in solutions:
        output_file.write(solution[0] + "\n")