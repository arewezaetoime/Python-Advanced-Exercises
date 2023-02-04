from collections import deque

names = deque()
for _ in range(int(input())):
    current_name = input()
    names.append(current_name)

unique_names = set(names)
for n in unique_names:
    print(n)
