symbols = dict()

for letter in input():
    symbols[letter] = symbols.get(letter, 0) + 1

for letter, count in sorted(symbols.items()):
    print(f'{letter}: {count} time/s')