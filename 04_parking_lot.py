def print_func(data):
    if data:
        for number_plate in data:
            print(number_plate)
    else:
        print('Parking Lot is Empty')


parking_lot = set()

COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'

for _ in range(int(input())):
    command, plate = input().split(', ')
    if command == COMMAND_IN:
        parking_lot.add(plate)
    elif command == COMMAND_OUT:
        parking_lot.remove(plate)

print_func(parking_lot)