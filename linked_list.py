#!/usr/bin/python
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next_node = node_B
    node_B.next_node = node_D
    node_D.next_node = node_E


def delete_node(del_data):
    global node_A
    pre_node = node_A
    nex_node = pre_node.next_node

    # Delete First Node
    if pre_node.data == del_data:
        node_A = nex_node
        del pre_node

    # Delete non-first Node
    while nex_node:
        if nex_node.data == del_data:
            pre_node.next_node = nex_node.next_node
            del nex_node
            break
        pre_node = nex_node
        nex_node = nex_node.next_node


def insert_node(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next_node
    new_node.next_node = node_T
    node_P.next_node = new_node


def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next_node


if __name__ == '__main__':
    print("Initialize Linked List")
    init_list()
    print_list()
    print("After Deleting node D")
    delete_node("D")
    print_list()
    print("After Adding node C")
    insert_node("C")
    print_list()