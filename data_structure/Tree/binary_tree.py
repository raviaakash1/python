class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.root = None
    def addChild(self, parent, child):
        if not parent.left:
            parent.left = child
            return True
        elif not parent.right:
            parent.right = child
            return True
        else:
            isAdded = self.addChild(parent.left, child)
            if isAdded:
                return True
            isAdded = self.addChild(parent.right, child)
            if isAdded:
                return True

    def traverse(self, root):
        if root is None:
            return 
        else:
            self.traverse(root.left)
            print(root.data, end = " ")
            self.traverse(root.right)

if __name__ == "__main__":
    root = Node(4)
    n1 = Node(12)
    n2 = Node(15)
    n3 = Node(22)
    n4 = Node(27)
    n5 = Node(2)
    n6 = Node(7)
    n7 = Node(127)
    n8 = Node(227)

    tree = Tree()
    tree.root = root
    tree.addChild(root, n1)
    tree.addChild(root, n3)
    tree.addChild(root, n4)
    tree.addChild(root, n2)
    tree.traverse(tree.root)