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
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_B.prev = node_A
    node_D.next = node_E
    node_D.prev = node_B
    node_E.prev = node_D


def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next
    next_next_node = next_node.next

    if pre_node.data == del_data:
        node_A = next_node
        del pre_node
        return

    while next_node:
        if next_node.data == del_data:
            next_next_node = next_node.next
            pre_node.next = next_node.next
            next_next_node.prev = next_node.prev
            del next_node
            break



def insert_node(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next
    new_node.next = node_T
    node_P.next = new_node
    new_node.prev = node_P
    node_T.prev = new_node



def print_list():
    global node_A
    node = node_A
    print(node.data)
    while node:
        print(node.data)
        node = node.next


if __name__ == '__main__':
    print("Initialize Doubly Linked List")
    init_list()
    print_list()
    print("Insert Node C")
    insert_node("C")
    print_list()
    print("Delete Node D")
    delete_node("D")
    print_list()
