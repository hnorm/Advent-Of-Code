#!/usr/bin/env python3


def part_one(file):
    return(min(main(file)))


def part_two(file):
    return(max(main(file)))


def main(file):
    distances = dict()
    cities = set([s.strip().split(" ")[0] for s in open(file)])
    cities.update([s.strip().split(" ")[2] for s in open(file)])

    for city in cities:
        distances[city] = dict()

    for line in open(file):
        args = line.strip().split(" ")
        distances[args[0]][args[2]] = int(args[4])
        distances[args[2]][args[0]] = int(args[4])

    record = []
    for city in distances:
        travel_to_next_city(record, distances, [city], 0)

    return record


def travel_to_next_city(record, distances, cities_travelled, distance_travelled):
    if len(distances) == len(cities_travelled):
        record.append(distance_travelled)
    else:
        for city in distances:
            if city not in cities_travelled:
                distance_to_next_city = distances[cities_travelled[-1]][city]
                new_cities_travelled = cities_travelled.copy()
                new_cities_travelled.append(city)
                travel_to_next_city(record, distances, new_cities_travelled, distance_travelled + distance_to_next_city)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(part_one("2015_09_distances.txt"))
    print(part_two("2015_09_distances.txt"))