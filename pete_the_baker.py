def cakes(recipe, available):
    res = float('inf')
    if len(available) == 0:
        return 0
    for k, v in recipe.items():
        res = min(res, available.get(k, 0) // v)
        if not res:
            return 0

    return res


if __name__ == '__main__':
    recipe = {"flour": 500, "sugar": 200, "eggs": 10}
    available = {"flour": 5500, "sugar": 1200, "eggs": 8, "milk": 200}
    available = {"flour": 5500, "sugar": 1200, "eggs": 8, "milk": 200}
    available = {}
    print(cakes(recipe, available))
