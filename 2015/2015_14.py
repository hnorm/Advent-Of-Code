#!/usr/bin/env python3

from collections import defaultdict

def part_one():
    speeds = [line.strip() for line in open(r"2015\2015_14_reindeer.txt")]
    print(max(distance_flown(deer, 2503) for deer in speeds))

def part_two():
    speeds = [line.strip() for line in open(r"2015\2015_14_reindeer.txt")]
    print(race(speeds, 2503))

def race(speeds, seconds):
    """
    >>> speeds = ["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.", "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."]
    >>> race(speeds, 1000)
    689
    """
    scoreboard = defaultdict(int)
    for s in range(1, seconds + 1):
        rank = [[deer, distance_flown(deer, s)] for deer in speeds]
        winner = max(rank, key = lambda i: i[1])
        scoreboard[winner[0]] += 1
    scoreboard[winner[0]] += 1
    return max(scoreboard.values())

def distance_flown(reindeer, seconds):
    """
    >>> distance_flown("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.", 1000)
    1120
    >>> distance_flown("Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.", 1000)
    1056
    """
    reindeer = reindeer.split(" ")
    speed = int(reindeer[3])
    fly_time = int(reindeer[6])
    rest_time = int(reindeer[13])

    seconds_flown = (seconds // (fly_time + rest_time)) * fly_time
    seconds_left = seconds % (fly_time + rest_time)
    return speed * (seconds_flown + min(seconds_left, fly_time))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    part_one()
    part_two()