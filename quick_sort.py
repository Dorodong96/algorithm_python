#!/usr/bin/python
import random
import time

compare_counter = 0
swap_counter = 0


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
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


if __name__ == '__main__':
    q_list = []
    input_n = input("The number of data to sort: ")
    for i in range(int(input_n)):
        q_list.append(random.randint(1, int(input_n)))
    print(" < Before Sort > ")
    print(q_list)

    start_time = time.time()
    quickSort(q_list)
    running_time = time.time() - start_time

    print(" < After Sort > ")
    print(q_list)