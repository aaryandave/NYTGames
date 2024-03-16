center_letter = "t"
table_letters = set("gniahb")
table_letters.add(center_letter)

valid_words = set()

# Preprocess the dictionary to remove unnecessary characters
with open('../../wordlist.txt', 'r') as input_dict_file:
    for line in input_dict_file:
        word = line.strip().lower().replace("'", '')
        if len(word) > 3 and center_letter in word and all(letter in table_letters for letter in word):
            valid_words.add(word)

print(f'Num Words: {len(valid_words)}')
print(sorted(valid_words, key=lambda x: len(x), reverse=True)) 
