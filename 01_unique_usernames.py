n_times = int(input())
usernames = set()

for _ in range(n_times):
    user = input()
    usernames.add(user)

print('\n'.join(usernames))