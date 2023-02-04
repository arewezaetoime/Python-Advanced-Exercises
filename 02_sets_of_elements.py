n, m = input().split()
n_set = set(input() for x in range(int(n)))
m_set = set(input() for y in range(int(m)))

print('\n'.join(n_set.intersection(m_set)))
