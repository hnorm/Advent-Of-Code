#!/usr/bin/env python3

import re
import json


def part_one():
    for line in open(r"2015\2015_12_data.txt"):
        return count(line)


def count(input):
    """
    >>> count('[1,2,3]')
    6
    >>> count('{"a":2,"b":4}')
    6
    >>> count('[[[3]]]')
    3
    >>> count('{"a":{"b":4},"c":-1}')
    3
    >>> count('{"a":[-1,1]}')
    0
    >>> count('[-1,{"a":1}]')
    0
    """

    result = re.split('[]()[{}:",]', input)

    count = 0
    for n in result:
        try:
            count += int(n)
        except:
            pass
    return count


def part_two():
    for line in open(r"2015\2015_12_data.txt"):
        return count_objects(json.loads(line))

    
def count_objects(objects):
    """
    >>> count_objects("1")
    1
    >>> count_objects("ten")
    0
    >>> x = [1, 2, 3]
    >>> count_objects(x)
    6
    >>> x = [1, {"c":"red", "b":2}, 3]
    >>> count_objects(x)
    4
    >>> x = {"d":"red","e":[1,2,3,4],"f":5}
    >>> count_objects(x)
    0
    >>> x = [1,"red",5]
    >>> count_objects(x)
    6
    """
    # value
    try:
        return int(objects)
    except:
        pass
        
    # string
    if isinstance(objects, str):
        return 0

    # dictionary
    try:
        if "red" in objects.values():
            return 0
        else:
            count = 0
            for i in objects.values():
                count += count_objects(i)
            return count
    except:
        pass

    # list
    try:
        count = 0
        for i in objects:
            count += count_objects(i)
        return count
    except:
        pass
        

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(part_one())
    print(part_two())