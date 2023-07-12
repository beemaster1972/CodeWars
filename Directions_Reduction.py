def dirReduc(arr):
    directions = {'NORTH': 'SOUTH', 'WEST': 'EAST', 'EAST': 'WEST', 'SOUTH': 'NORTH'}
    i, j = 0, 1
    res = arr[:]
    while i < j < len(arr):
        if res[i] == directions[res[j]]:
            res.pop(i)
            res.pop(i)
        else:
            i += 1
            j += 1
    return res


if __name__ == '__main__':
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    u = ["NORTH", "WEST", "SOUTH", "EAST"]

    print(dirReduc(a))
    print(dirReduc(u))
