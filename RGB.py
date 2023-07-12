def rgb(r, g, b):
    # your code here :)
    def rounding_to_nearest_byte(num):
        if num < 0:
            return 0
        elif num > 255:
            return 255
        else:
            return num

    r = rounding_to_nearest_byte(r)
    g = rounding_to_nearest_byte(g)
    b = rounding_to_nearest_byte(b)
    return hex(r).upper()[2:].zfill(2) + hex(g).upper()[2:].zfill(2) + hex(b).upper()[2:].zfill(2)


if __name__ == '__main__':
    print(rgb(1, 2, 3))
