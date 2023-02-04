elements = set()

for _ in range(int(input())):
    current_elements = input().split()
    for el in current_elements:
        elements.add(el)

print(*elements, sep='\n')
