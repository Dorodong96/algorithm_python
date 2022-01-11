#!/usr/bin/python
import random
import time


def shell_sort(random_list):
    h = 1
    while h < len(random_list):
        h = h * 3 + 1
    h = h // 3  # h = 40 for MAX = 100

    while h > 0:
        for i in range(h):
            start_index = i + h

            while start_index < len(random_list):
                temp = random_list[start_index]
                insert_index = start_index
                print(start_index)
                while insert_index > h - 1 and random_list[insert_index - h] > temp:
                    random_list[insert_index] = random_list[insert_index - h]
                    insert_index -= h
                    print("loop2")
                random_list[insert_index] = temp  # random_list[0] = random_list[40]
                start_index = start_index + h
            h = h // 3


if __name__ == '__main__':
    s_list = []
    input_n = input("The number of Data to Sort: ")
    for i in range(int(input_n)):
        s_list.append(random.randint(1, int(input_n)))
    print(" < Before Sort > ")
    print(s_list)

    start_time = time.time()
    shell_sort(s_list)
    running_time = time.time() - start_time
    print(" < After Sort > ")
    print(s_list)

    print("Size of Data: {}".format(int(input_n)))
    print("Execution Time: {}".format(running_time))
