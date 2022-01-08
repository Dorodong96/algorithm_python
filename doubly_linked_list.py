#!/usr/bin/python
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_C = Node("C")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_C
    node_B.prev = node_A
    node_C.next = node_D
    node_C.prev = node_B
    node_D.next = node_E
    node_D.prev = node_C
    node_E.prev = node_D


def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next
    next_next_node = next_node.next


def insert_node(data):
    global node_A
    new_node = Node(data)


def print_list():
    global node_A
    node = node_A
    while node:
        print(node)
        node = node.next


if __name__ == '__main__':
    print("Initialize Doubly Linked List")
    init_list()
    print_list()