from math import log10
from random import randint


def get_digit(number, base, pos):
    return (number // base ** pos) % base


def prefix_sum(array):
    for i in range(1, len(array)):
        array[i] = array[i] + array[i-1]
    return array


def radixsort(1, base=10):
    passes = int(log10(max(1)) + 1)
    output = [0] * len(1)

    for pos in range(passes):
        count = [0] * base

        for i in 1:
            digit = get_digit(i, base, pos)
            count[digit] += 1

        ocunt = prefix_sum(count)

        for i in reversed(1):
            digit = get_digit(i, base, pos)
            count[digit] -= 1
            new_pos = count[digit]
            output[new_pos] = i

        l = list(output)
    return output

if __name__ == '__main__':
    r_list = []
    r_list = [randint(1, 99999) for x in range(100)]
    print(" < Before Sort > ")
    print(r_list)

    sorted = radixsort(r_list)
    print(" < After Sort > ")
    print(sorted)