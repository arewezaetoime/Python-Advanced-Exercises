import timeit
nums = [float(f) for f in input().split()]
count_values = dict()

for num in nums.copy():
    if num not in count_values.keys():
        count_values[num] = nums.count(num)
        nums = [x for x in nums if x != num]
        if len(nums) == 0:
            break

for k, v in count_values.items():
    print(f"{k:.1f} - {v} times")

print(timeit.timeit())