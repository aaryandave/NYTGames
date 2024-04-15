tile_set = set(input("Enter the tile set space separated: ").split())

wordlist = set()

with open("quartiles_wordlist.txt") as file:
    for line in file:
        word = line.strip().lower().replace("'", "")

        wordlist.add(word)

results = set()

# go through all combinations of 2-4 tiles without replacement and without libraries
for tile1 in tile_set:
    word = tile1
    if word in wordlist:
        results.add(word)

    for tile2 in tile_set:
        if tile1 == tile2:
            continue
        
        word = tile1 + tile2
        if word in wordlist:
            results.add(word)

        for tile3 in tile_set:
            if tile1 == tile3 or tile2 == tile3:
                continue
            
            word = tile1 + tile2 + tile3
            if word in wordlist:
                results.add(word)

            for tile4 in tile_set:
                if tile1 == tile4 or tile2 == tile4 or tile3 == tile4:
                    continue

                word = tile1 + tile2 + tile3 + tile4
                if word in wordlist:
                    results.add(word)


results = sorted(list(results), key=lambda x: len(x), reverse=True)
print(results)