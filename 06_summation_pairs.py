numbers = list(map(int, input().split()))
target = int(input())

potential_nums = [x for x in numbers if x < target]

targets = set()
values_map = {}

for number in potential_nums:
    if number in targets:
        targets.remove(number)
        pair = values_map[number]
        del values_map[number]
        print(f'{pair} + {number} = {target}')
    else:
        resulting_number = target - number
        targets.add(resulting_number)
        values_map[resulting_number] = number
