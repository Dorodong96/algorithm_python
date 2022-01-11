#!/usr/bin/python
import random
import time

compare_counter = 0
swap_counter = 0


def bubble_sort(random_list):
    global compare_counter, swap_counter
    for start_index in range(len(random_list) - 1):
        for index in range(1, len(random_list) - start_index):
            compare_counter += 1
            if random_list[index - 1] > random_list[index]:
                random_list[index - 1], random_list[index] = random_list[index], random_list[index - 1]
                swap_counter += 1


if __name__ == '__main__':
    b_list = []
    input_n = input("Data to Sort: ")
    for i in range(int(input_n)):
        b_list.append(random.randint(1, int(input_n)))

    print(" < Before Sort > ")
    print(b_list)
    print()

    start_time = time.time()
    bubble_sort(b_list)
    running_time = time.time() - start_time

    print(" < After Sort > ")
    print(b_list)
    print()

    print("Size of Data: {}".format(int(input_n)))
    print("Compare Times: {}".format(compare_counter))
    print("Swap Times: {}".format(swap_counter))
    print("Execution Time: {}".format(running_time))