#!/usr/bin/env python3

import re
import json

def part_one():
    aunts = load_aunties()
    candidates = list(aunts.keys())
    signature = load_MFCSAM()
    for aunt, items in aunts.items():
        for item, count in items.items():
            if item in signature and signature[item] != int(count):
                candidates.remove(aunt)
                break
        
    print(candidates)

def part_two():
    aunts = load_aunties()
    candidates = list(aunts.keys())
    signature = load_MFCSAM()
    for aunt, items in aunts.items():
        for item, count in items.items():
            if item in signature:
                fail = False
                if item in ['cats', 'trees']:
                    if int(count) < signature[item]:
                        fail = True
                elif item in ['pomeranians', 'goldfish']:
                    if int(count) > signature[item]:
                        fail = True
                else:
                    if int(count) != signature[item]:
                        fail = True

                if fail:
                    candidates.remove(aunt)
                    break
        
    print(candidates)


def load_aunties():
    aunts = dict()
    for line in open(r"2015\2015_16_aunts.txt"):
        match = re.match("Sue (?P<id>\d*): (?P<stuff>.*)", line.strip())
        items = re.findall("(\w*): (\d*)", match['stuff'])
        aunts[match['id']] = dict()
        for item in items:
            aunts[match['id']][item[0]] = item[1]

    return aunts


def load_MFCSAM():
    return ({
        'children': 3, 
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1})

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    part_one()
    part_two()