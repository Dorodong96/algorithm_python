#!/usr/bin/python
from math import log10
from random import randint

global counter_rec


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[lmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            swap(x, lmark, rmark)
            lmark += 1
            rmark -= 1
    swap(x, pivot_idx, rmark)
    return rmark


def quickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        if first < last:
            splitpoint = pivotMethod(x, first, last)
            _qsort(x, first, splitpoint-1)
            _qsort(x, splitpoint+1, last)
    _qsort(x, 0, len(x)-1)


def binary_search(a_list, wanted_data):
    global counter_rec
    first = 0
    last = len(a_list) - 1

    while first <= last:
        idx = (first + last) // 2
        counter_rec += 1
        if a_list[idx] == wanted_data:
            print('{item} found at position {i}'.format(item=wanted_data, i=idx))
            return True
        elif a_list[idx] > wanted_data:
            last = idx - 1
        elif a_list[idx] < wanted_data:
            first = idx + 1
        else:
            print('{item} not found in the list'.format(item=wanted_data))
            return False


def binary_search_recursive(a_list, wanted_data):
    global counter_rec
    first = 0
    last = len(a_list) - 1

    if len(a_list) == 0:
        print('{item} not found in the list'.format(item=wanted_data))
        return False
    else:
        idx = (first + last) // 2
        counter_rec += 1
        if wanted_data == a_list[idx]:
            print('{item} found at position {i}'.format(item=wanted_data, i=idx))
            return True
        else:
            if a_list[idx] < wanted_data:
                return binary_search_recursive(a_list[idx+1:], wanted_data)
            else:
                return binary_search_recursive(a_list[:idx], wanted_data)


if __name__ == '__main__':
    data = []
    counter_rec= 0
    input_n = input("The number of Total data: ")
    data = [randint(1, 100) for x in range(int(input_n))]

    print(" < After Sort > ")
    quickSort(data)
    print(data)

    msg = binary_search_recursive(data, 50)
    if msg:
        print("Found {} for {} times of comparison".format(50, counter_rec))
    print(msg)
