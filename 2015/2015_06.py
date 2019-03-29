#!/usr/bin/env python3


def part_one(file):

    lights = [[False for j in range(1000)] for i in range(1000)]

    for line in open(file):
        do_action(lights, line.strip())

    return sum(1 for x in lights for i in x if i)


def do_action(lights, instruction):
    """
    >>> from collections import defaultdict
    >>> lights = [[0 for j in range(2)] for i in range(2)]
    >>> do_action(lights, "turn on 0,0 through 1,1")
    [[1, 1], [1, 1]]
    >>> do_action(lights, "turn off 0,0 through 1,1")
    [[0, 0], [0, 0]]
    >>> do_action(lights, "toggle 0,0 through 0,0")
    [[1, 0], [0, 0]]
    """
    action = instruction.split(" ")

    if "on" in action:
        start = [int(i) for i in action[2].split(",")]
        end = [int(i) for i in action[4].split(",")]
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                lights[i][j] = True

    elif "off" in action:
        start = [int(i) for i in action[2].split(",")]
        end = [int(i) for i in action[4].split(",")]
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                lights[i][j] = False
    else:
        start = [int(i) for i in action[1].split(",")]
        end = [int(i) for i in action[3].split(",")]
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                lights[i][j] = not lights[i][j]

    return lights


def part_two(file):

    lights = [[0 for j in range(1000)] for i in range(1000)]

    for line in open(file):
        do_action_two(lights, line.strip())

    return sum([sum(x) for x in lights])


def do_action_two(lights, instruction):
    """
    >>> from collections import defaultdict
    >>> lights = [[0 for j in range(2)] for i in range(2)]
    >>> do_action_two(lights, "turn on 0,0 through 1,1")
    [[1, 1], [1, 1]]
    >>> do_action_two(lights, "toggle 0,0 through 1,1")
    [[3, 3], [3, 3]]
    >>> do_action_two(lights, "turn off 0,0 through 1,1")
    [[2, 2], [2, 2]]
    >>> do_action_two(lights, "toggle 0,0 through 0,0")
    [[4, 2], [2, 2]]
    """
    action = instruction.split(" ")

    if "on" in action:
        start = [int(i) for i in action[2].split(",")]
        end = [int(i) for i in action[4].split(",")]
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                lights[i][j] += 1

    elif "off" in action:
        start = [int(i) for i in action[2].split(",")]
        end = [int(i) for i in action[4].split(",")]
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                lights[i][j] = max(0, lights[i][j] - 1)

    else:
        start = [int(i) for i in action[1].split(",")]
        end = [int(i) for i in action[3].split(",")]
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                lights[i][j] += 2

    return lights


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(part_one(r"2015\2015_06_instructions.txt"))
    print(part_two(r"2015\2015_06_instructions.txt"))