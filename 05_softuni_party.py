guests = {input() for _ in range(int(input()))}
randoms = set()

command = input()
while command != 'END':
    randoms.add(command)
    command = input()

guest_who_did_not_came = guests.difference(randoms)
print(len(guest_who_did_not_came))
if guest_who_did_not_came:
    for guest in sorted(guest_who_did_not_came):
        print(guest)
