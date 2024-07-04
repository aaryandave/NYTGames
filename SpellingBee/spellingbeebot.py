"""NYTGames Spelling Bee Solver
"""
center_letter = input("Center letter: ")
remaining_letters = set(input("Remaining letters: "))
remaining_letters.add(center_letter)

valid_words = set()

# preprocess the dictionary to remove unnecessary characters
with open('../../wordlist.txt', 'r', encoding="utf-8") as input_dict_file:
    for line in input_dict_file:
        word = line.strip().lower()
        if len(word) > 3 and center_letter in word and all(letter in
                                                           remaining_letters for letter in word):
            valid_words.add(word)

print(f'Num Words: {len(valid_words)}')
valid_words_list: list = sorted(valid_words, key=len, reverse=True)
print("Longest words: ", valid_words_list[:5])

# write the words to spellingbee_solutions.txt
with open('spellingbee_solutions.txt', 'w', encoding="utf-8") as output_file:
    output_file.write(f"Num Words: {len(valid_words)}\n")
    for word in valid_words:
        output_file.write(word + "\n")

print("Remaining solutions in spellingbee_solutions.txt.")
