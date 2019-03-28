#!/usr/bin/env python3


def part_one(file):
    instructions = [line.strip() for line in open(file)]
    wires = run(instructions)
    return wires['a']


def part_two(file):
    instructions = [line.strip() for line in open(file)]
    wires = run(instructions)
    wires['b'] = wires['a']
    wires = run(instructions, wires)
    return wires['a']


def run(instructions, wires = None):
    """ 
    >>> instructions = "123 -> x, 456 -> y, x AND y -> d, x OR y -> e, x LSHIFT 2 -> f, y RSHIFT 2 -> g, NOT x -> h, NOT y -> i".split(", ")
    >>> run(instructions)
    {'x': 123, 'y': 456, 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079}
    """

    if wires == None:
        wires = dict()
        initialise_variables(wires, instructions)

    for _ in range(len(instructions)):
        for action in instructions:
            if "AND" in action:
                and_gate(wires, action)
            elif "OR" in action:
                or_gate(wires, action)
            elif "NOT" in action:
                not_gate(wires, action)
            elif "LSHIFT" in action:
                left_shift_gate(wires, action)
            elif "RSHIFT" in action:
                right_shift_gate(wires, action)
            else:
                assign_variable(wires, action)

    return wires


def initialise_variables(wires, instructions):
    """
    >>> wires = dict()
    >>> instructions = ["123 -> x"]
    >>> initialise_variables(wires, instructions)
    {'x': 123}
    >>> instructions = ["x AND y -> d"]
    >>> initialise_variables(wires, instructions)
    {'x': 123}
    >>> instructions = ["NOT x -> h"]
    >>> initialise_variables(wires, instructions)
    {'x': 123}
    """
    for action in instructions:
        action_args = action.split(" ")
        if len(action_args) == 3:
            if action_args[0].isnumeric():
                wires[action_args[2]] = int(action_args[0])
    return wires


def assign_variable(wires, action):
    """
    >>> wires = {'x': 123}
    >>> action = "x -> y"
    >>> assign_variable(wires, action)
    >>> wires
    {'x': 123, 'y': 123}
    """
    action_args = action.split(" ")
    if action_args[0] in wires.keys():
        wires[action_args[2]] = wires[action_args[0]]


def and_gate(wires, action):
    """
    >>> wires = {'x': 123, 'y': 456}
    >>> action = "x AND y -> d"
    >>> and_gate(wires, action)
    >>> wires
    {'x': 123, 'y': 456, 'd': 72}
    """
    action_args = action.split(" ")

    if action_args[0].isnumeric():
        val1 = int(action_args[0])
    elif action_args[0] in wires.keys():
        val1 = wires[action_args[0]]
    else:
        return

    if action_args[2].isnumeric():
        val2 = int(action_args[2])
    elif action_args[2] in wires.keys():
        val2 = wires[action_args[2]]
    else:
        return

    wires[action_args[4]] = val1 & val2


def left_shift_gate(wires, action):
    """
    >>> wires = {'x': 123}
    >>> action = "x LSHIFT 2 -> f"
    >>> left_shift_gate(wires, action)
    >>> wires
    {'x': 123, 'f': 492}
    """
    action_args = action.split(" ")
    if action_args[0] in wires.keys():
        wires[action_args[4]] = wires[action_args[0]] << int(action_args[2])


def right_shift_gate(wires, action):
    """
    >>> wires = {'x': 456}
    >>> action = "x RSHIFT 2 -> aa"
    >>> right_shift_gate(wires, action)
    >>> wires
    {'x': 456, 'aa': 114}
    """
    action_args = action.split(" ")
    if action_args[0] in wires.keys():
        wires[action_args[4]] = wires[action_args[0]] >> int(action_args[2])

    if action == "x RSHIFT 2 -> aa":
        pass

def not_gate(wires, action):
    """
    >>> wires = {'x': 123, 'y': 456}
    >>> action = "NOT x -> h"
    >>> not_gate(wires, action)
    >>> action = "NOT y -> i"
    >>> not_gate(wires, action)
    >>> action = "NOT i -> j"
    >>> not_gate(wires, action)
    >>> wires
    {'x': 123, 'y': 456, 'h': 65412, 'i': 65079, 'j': 456}
    """
    action_args = action.split(" ")
    if action_args[1] in wires.keys():
        wires[action_args[3]] = 65535 + ~ wires[action_args[1]] + 1


def or_gate(wires, action):
    """
    >>> wires = {'x': 123, 'y': 456}
    >>> action = "x OR y -> e"
    >>> or_gate(wires, action)
    >>> wires
    {'x': 123, 'y': 456, 'e': 507}
    >>> action = "x OR 456 -> f"
    >>> or_gate(wires, action)
    >>> wires
    {'x': 123, 'y': 456, 'e': 507, 'f': 507}
    >>> wires = dict()
    >>> action = "z OR 456 -> g"
    >>> or_gate(wires, action)
    >>> wires
    {}
    """
    action_args = action.split(" ")

    if action_args[0].isnumeric():
        val1 = int(action_args[0])
    elif action_args[0] in wires.keys():
        val1 = wires[action_args[0]]
    else:
        return

    if action_args[2].isnumeric():
        val2 = int(action_args[2])
    elif action_args[2] in wires.keys():
        val2 = wires[action_args[2]]
    else:
        return

    wires[action_args[4]] = val1 | val2



if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    # print(part_one("2015_07_instructions.txt"))
    print(part_two("2015_07_instructions.txt"))