#!/usr/bin/env python3


def part_one():
    result = str(1113122113)

    for i in range(40):
        result = say(result)

    return len(result)


def part_two():
    result = str(1113122113)

    for i in range(50):
        result = say(result)

    return len(result)

    
def say(input):
    """
    >>> say(1)
    11
    >>> say(11)
    21
    >>> say(21)
    1211
    >>> say(1211)
    111221
    >>> say(111221)
    312211
    """

    result = ""

    current_number = input[0]
    count = 1
    for d in input[1:]:
        if current_number == d:
            count += 1
        else:
            result += str(count)
            result += current_number
            current_number = d
            count = 1
    
    result += str(count)
    result += current_number

    return result


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(part_one())
    print(part_two())