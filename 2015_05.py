#!/usr/bin/env python3

def part_one(file):
    return [is_nice(line) for line in open(file, "r")].count(True)
        
def part_two(file):
    return [is_nice_two(line) for line in open(file, "r")].count(True)
        
def is_nice(s_input):
    """
    >>> is_nice("ugknbfddgicrmopn")
    True
    >>> is_nice("aaa")
    True
    >>> is_nice("jchzalrnumimnmhp")
    False
    >>> is_nice("haegwjzuvuyypxyu")
    False
    >>> is_nice("dvszwmarrgswjxmb")
    False
    """

    input_list = [c for c in s_input]

    vowels = [c for c in "aeiou"]
    count = 0
    for v in vowels:
        count += input_list.count(v)
    if count < 3:
        return False

    passed = False
    for i in range(1, len(input_list)):
        if input_list[i] == input_list[i-1]:
            passed = True
            break
    if not passed:
        return False

    prohibited = ["ab", "cd", "pq", "xy"]
    for cc in prohibited:
        if cc in s_input:
            return False

    return True

def is_nice_two(s_input):
    """
    >>> is_nice_two("qjhvhtzxzqqjkmpb")
    True
    >>> is_nice_two("xxyxx")
    True
    >>> is_nice_two("uurcxstgmygtbstg")
    False
    >>> is_nice_two("ieodomkazucvgmuy")
    False
    """

    def test_one(s_input):
        for i in range(len(s_input) - 1):
            cc = s_input[i:i+2]
            if cc in s_input[i+2:]:
                return True
        return False

    def test_two(s_input):
        for i in range(2, len(s_input)):
            if s_input[i] == s_input[i-2]:
                return True
        return False

    return test_one(s_input) and test_two(s_input)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(part_one("2015_05_strings.txt"))
    print(part_two("2015_05_strings.txt"))