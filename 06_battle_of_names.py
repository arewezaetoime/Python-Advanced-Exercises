odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    name = input()
    char_sum = sum(ord(let) for let in name) // row
    if char_sum % 2 == 0:
        even_set.add(char_sum)
    else:
        odd_set.add(char_sum)

if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
elif sum(even_set) > sum(odd_set):
    print(*odd_set.symmetric_difference(even_set), sep=', ')
else:
    print(*odd_set.union(even_set), sep=', ')
