#!/usr/bin/env python3


from itertools import permutations


def part_one(ingredients):
    print(max([get_score(r, ingredients) for r in get_all_recipes(ingredients)]))

def part_two(ingredients):
    print(max([get_score_two(r, ingredients) for r in get_all_recipes(ingredients)]))

def get_all_recipes(ingredients):
    recipes = []
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - (a+b)):
                d = 100 - (a+b+c)
                recipes.append([a, b, c, d])
    return recipes


def get_score(recipe, ingredients):
    names = list(ingredients.keys())
    capacity = sum(recipe[i] * ingredients[names[i]]["capacity"] for i in range(4))
    durability = sum(recipe[i] * ingredients[names[i]]["durability"] for i in range(4))
    flavor = sum(recipe[i] * ingredients[names[i]]["flavor"] for i in range(4))
    texture = sum(recipe[i] * ingredients[names[i]]["texture"] for i in range(4))
    
    if capacity > 0 and durability > 0 and flavor > 0 and texture > 0:
        return capacity * durability * flavor * texture
    else:
        return 0

def get_score_two(recipe, ingredients):
    names = list(ingredients.keys())
    capacity = sum(recipe[i] * ingredients[names[i]]["capacity"] for i in range(4))
    durability = sum(recipe[i] * ingredients[names[i]]["durability"] for i in range(4))
    flavor = sum(recipe[i] * ingredients[names[i]]["flavor"] for i in range(4))
    texture = sum(recipe[i] * ingredients[names[i]]["texture"] for i in range(4))
    calories = sum(recipe[i] * ingredients[names[i]]["calories"] for i in range(4))

    if capacity > 0 and durability > 0 and flavor > 0 and texture > 0 and calories == 500:
        return capacity * durability * flavor * texture
    else:
        return 0

if __name__ == "__main__":
    ingredients = ({
        "Sprinkles":    {"capacity":5, "durability":-1, "flavor":0, "texture":0, "calories":5}, 
        "PeanutButter": {"capacity":-1, "durability":3, "flavor":0, "texture":0, "calories":1},
        "Frosting":     {"capacity":0, "durability":-1, "flavor":4, "texture":0, "calories":6},
        "Sugar":        {"capacity":-1, "durability":0, "flavor":0, "texture":2, "calories":8}
        })

    import doctest
    doctest.testmod()
    part_one(ingredients)
    part_two(ingredients)