#!/usr/bin/env python3


def part_one(file):
    count = 0
    s_value = ""
    for line in open(file):
        count += count_string(line.strip())
    return count


def count_string(s_string):
    """
    >>> s = '""'
    >>> count_string(s)
    2
    >>> s = '"abc"'
    >>> count_string(s)
    2
    """
    s_value = eval(s_string)
    return len(s_string) - len(s_value)


def part_two(file):
    count = 0
    s_value = ""
    for line in open(file):
        count += count_string_two(line.strip())
    return count


def count_string_two(s_string):
    """
    >>> s = '""'
    >>> count_string_two(s)
    6
    >>> s = '"abc"'
    >>> count_string_two(s)
    6
    """
    count = 0
    for i in range(len(s_string)):
        if s_string[i] in ['"', '\\']:
            count += 1

    return len(s_string) + count + 2 - len(s_string)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(part_one("2015_08_strings.txt"))
    print(part_two("2015_08_strings.txt"))