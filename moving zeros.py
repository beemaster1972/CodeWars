def move_zeros(lst):
    if sum(lst) == 0:
        return lst
    i = 0
    j = 0
    while j < len(lst) and i < len(lst):
        if lst[i]:
            i += 1
            continue
        else:
            lst.append(lst.pop(i))
        j += 1
    return lst


if __name__ == '__main__':
    lst1 = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
    lst2 = [1, 2, 1, 1, 3, 1]
    lst3 = move_zeros(lst2[:])
    lst4 = move_zeros(lst1[:])
    print(lst1)
    print(lst4)
    print(lst2)
    print(lst3)
