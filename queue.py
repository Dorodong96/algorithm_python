#!/usr/bin/python

def put(item):
    queue.append(item)


def get():
    return queue.pop()


if __name__ == '__main__':
    queue = [] # queue create
    put(1)
    put(2)
    put(3)
    put(4)

    print("Current Queue Form")
    print(queue)

    while queue:
        print("POP > {}".format(get()))
