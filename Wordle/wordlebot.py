wrong_letters = [letter for letter in '']
confirmed_letters = {0: "", 1: "", 2:"", 3: "", 4: ""}

# raise donut starting words
shift_letters = {}
words = []
input_dict_file = open('wordle_wordlist.txt', 'r')
for line in input_dict_file:    
    word = line.strip().lower().replace("'", '')
    allow = True
    if len(word) == 5:
        if not any(letter in word for letter in wrong_letters):
            if all(confirmed_letters[i] == "" or word[i] == confirmed_letters[i] for i in confirmed_letters.keys()):
                for letter in shift_letters.keys():
                    if not (letter in word and all(letter != word[ind] for ind in shift_letters[letter])):
                        allow = False
                if allow:
                    words.append(word)

words.sort(reverse=True, key=lambda x: len(set(x)))

print("Number of words: ", len(words))
print("Best 5 words: ", words[:5])

# write the words to wordle_solutions.txt
with open('wordle_solutions.txt', 'w') as output_file:
    print("Number of solutions: ", len(words))
    print("Best 5 solutions: ", words[:5])
    for word in words:
        output_file.write(word + "\n")