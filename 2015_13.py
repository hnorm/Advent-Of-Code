#!/usr/bin/env python3

from collections import defaultdict
from itertools import permutations


def part_one(input):
    """
    >>> part_one("2015_13_test_values.txt")
    330
    """
    values = load_values(input)
    guests = list(values.keys())
    return max(happiness(seating, values) for seating in get_possible_seatings(guests))


def part_two(input):
    values = load_values(input)
    guests = list(values.keys())
    
    for guest in guests:
        values[guest]['me'] == 0
        values['me'][guest] == 0

    guests.append('me')
    return max(happiness(seating, values) for seating in get_possible_seatings(guests))


def load_values(input):
    values = defaultdict(lambda: defaultdict(int))

    for line in open(input):
        line = line.strip()[:-1].split(" ")
        if line[2] == "gain":
            values[line[0]][line[-1]] = int(line[3])
        else:
            values[line[0]][line[-1]] = -int(line[3])

    return values


def get_possible_seatings(guests):
    perms = list(permutations(guests[1:]))
    anchor_seat = guests[0]
    result = []
    for perm in perms:
        re = perm[::-1]
        if re not in result:
            result.append(perm)
    return [[anchor_seat] + list(l) for l in result]


def happiness(guest_order, values):
    """
    >>> values = load_values("2015_13_test_values.txt")
    >>> guest_order = ["Alice"]
    >>> happiness(guest_order, values)
    0
    >>> guest_order = ["Alice", "Bob"]
    >>> happiness(guest_order, values)
    274
    >>> guest_order = ["Alice", "Bob", "Carol", "David"]
    >>> happiness(guest_order, values)
    330
    """
    if len(guest_order) <= 1:
        return 0
    elif len(guest_order) == 2:
        return 2*(values[guest_order[0]][guest_order[1]] + values[guest_order[1]][guest_order[0]])
    else:
        happiness = 0
        for i in range(len(guest_order)-1):
            happiness += values[guest_order[i]][guest_order[i-1]] + values[guest_order[i]][guest_order[i+1]]
        happiness += values[guest_order[-1]][guest_order[-2]] + values[guest_order[-1]][guest_order[0]]
        return happiness


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(part_one("2015_13_guest_list.txt"))
    print(part_two("2015_13_guest_list.txt"))