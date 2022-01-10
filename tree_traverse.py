class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def init_tree():
    global root

    new_node = Node("A")
    root = new_node
    new_node = Node("B")
    root.left = new_node
    new_node = Node("C")
    root.right = new_node
    new_node_1 = Node("D")
    new_node_2 = Node("E")
    node = root.left
    node.left = new_node_1
    node.right = new_node_2

    new_node_1 = Node("F")
    new_node_2 = Node("G")
    node = root.right
    node.left = new_node_1
    node.right = new_node_2


# Pre-Order Traverse (A -> B -> D -> E -> C -> F -> G)
def preorder_traverse(node):
    if node == None: return
    print(node.data, end=' -> ')
    preorder_traverse(node.left)
    preorder_traverse(node.right)


# In-Order Traverse (D -> B -> E -> A -> F -> C -> G)
def inorder_traverse(node):
    if node == None: return
    inorder_traverse(node.left)
    print(node.data, end=' -> ')
    inorder_traverse(node.right)


# Post-Order Traverse (D -> E -> B -> F -> G -> C -> A)
def postorder_traverse(node):
    if node == None: return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end=' -> ')


# Level-Order Traverse
levelq = []

def levelorder_traverse(node):
    global levelq
    levelq.append(node)
    while len(levelq) != 0:
        # visit
        visit_node = levelq.pop(0)
        print(visit_node.data, end=' -> ')
        # child put
        if visit_node.left != None:
            levelq.append(visit_node.left)
        if visit_node.right != None:
            levelq.append(visit_node.right)


# Traverse Program
if __name__ == '__main__':
    init_tree()
    print("<< Pre-Order Traverse >>")
    preorder_traverse(root)
    print("\n")
    print("<< In-Order Traverse >>")
    inorder_traverse(root)
    print("\n")
    print("<< Post-Order Traverse >>")
    postorder_traverse(root)
    print("\n")
    print("<< Level-Order Traverse >>")
    levelorder_traverse(root)
    print("\n")