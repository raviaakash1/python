Tree Data Structure

It is a non linear data structre where a collection of elements known as nodes are connected to each other via edges such that there exists exactly one path between any two nodes.

![tree](image.png)

Types of Tree:
    1. Binary Tree
    2. Ternary Tree
    3. N-ary tree


![types_of_tree](image-1.png)


A tree is a hierarchical data structre used to organize and represent data in a parent-child relationship.
It consists of nodes, where the topmmost node is called the root, and every other node can have one or more child nodes.

![tree_structure](image-2.png)
![level_height](image-3.png)
![sub_tree_struct](image-4.png)
![nomenclature](image-5.png)
![edge_def](image-6.png)

Basic Terminology:
    * Parent Node: A node that is an immediate predecessor of another node.
    * Child Node: A node that is an immediate successor of another node.
    * Root Node: The topmost node in a tree, which does not have a parent.
    * Lead Node(External Node): Node that do not have any children.
    * Ancestor: Ant node on the path from the root to a given node.
    * Descendant: A node x is adescendant of another node y if u is an ancestor of x.
    * Sibling: Node that share the same parent, 
    * Level of a node: The nuber of edges in the path from the rooot to that node. The root node is at level 0.
    * Internal Node: A node with at least one child.
    * Neighbour of a Node: The parent or children of a node.
    * Subtree: A node and all its descendants from a subtree.

Class representation of a Node in a Tree Data Structure:

# Node structure of a tree
    class Node:
        def __init__(self, x):
            self.data = x
            self.children = []

Types of Tree Data Structures :
    Tree data structures can be classified based on the number of children each node can have.

Binary Tree:
    Each node can have a maximum of two children.

    Full Binary Tree – every node has either 0 or 2 children.
    Complete Binary Tree – all levels are fully filled except possibly the last, which is filled from left to right.
    Balanced Binary Tree – height difference between left and right subtrees of every node is minimal.

Ternary Tree:
    Each node can have at most three children, often labeled as left, middle, and right.

    N-ary Tree (or Generic Tree):
    Each node can have any number of children.
    Each node typically contains: Some data , A list of references to its children (duplicates are not allowed).
    Unlike linked lists, nodes store references to multiple child nodes.
    Please refer Types of Trees in Data Structures(https://www.geeksforgeeks.org/dsa/types-of-trees-in-data-structures/) for details.

    