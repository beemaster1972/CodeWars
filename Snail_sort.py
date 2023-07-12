import numpy as np
def snail(snail_map):
    if len(snail_map) == 1:
        return snail_map[0]
    res = snail_map[0]
    trans = np.array(snail_map)
    while len(trans[1:]):
        trans = trans[1:]
        trans = np.rot90(trans)
        res.extend(trans[0])
    return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    snail_sort_matrix = snail(matrix)
    print(snail_sort_matrix)
