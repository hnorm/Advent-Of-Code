#!/usr/bin/env python3


def part_one():
    result = increment("hepxcrrq")
    while not test_1(result) or not test_2(result) or not test_3(result):
        result = increment(result)

    return result

def part_two():
    result = increment("hepxxyzz")
    while not test_1(result) or not test_2(result) or not test_3(result):
        result = increment(result)

    return result


def increment(input):
    """
    >>> increment("a")
    'b'
    >>> increment("abc")
    'abd'
    >>> increment("asd")
    'ase'
    >>> increment("zzz")
    'aaaa'
    """
    result = ""
    carry = False

    for i in range(len(input)-1, -1, -1):
        if input[i] == "z":
            result = "a" + result
            carry = True
        else:
            result = input[:i] + chr(ord(input[i]) + 1) + result
            carry = False
            break

    if carry:
        return "a" + result
    else:
        return result

def test_1(input):
    """
    >>> test_1("hijklmmn")
    True
    >>> test_1("abcdffaa")
    True
    >>> test_1("")
    False
    >>> test_1("abdfasdf")
    False
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(input)-3):
        if input[i:i+3] in alphabet:
            return True
    return False


def test_2(input):
    """
    >>> test_2("hijklmmn")
    False
    >>> test_2("abcdffaa")
    True
    >>> test_2("")
    True
    >>> test_2("abdfasdf")
    True
    """
    if "i" in input or "o" in input or "l" in input:
        return False
    return True


def test_3(input):
    """
    >>> test_3("abbceffg")
    True
    >>> test_3("abbcegjk")
    False
    >>> test_3("abcdffaa")
    True
    >>> test_3("ghjaabcc")
    True
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0

    for c in alphabet:
        if c + c in input:
            count += 1
            
    return count >= 2


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(part_one())
    print(part_two())