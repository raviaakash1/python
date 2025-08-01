

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    print("Output")
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    if head1 == None and head2 == None:
        return None
    if head1 == None:
        return head2
    elif head2 == None:
        return head1
    result = SinglyLinkedList()
    while True:
        
        if head1 == None and head2 != None:
            while head2:
                result.insert_node(head2.data)
                head2 = head2.next
            return result.head
            
        elif head2 == None and head1 != None:
            while head1:
                result.insert_node(head1.data)
                head1 = head1.next
            return result.head


        if head1.data <= head2.data:
            result.insert_node(head1.data)
            head1 = head1.next
        else:
            result.insert_node(head2.data)
            head2 = head2.next
        


if __name__ == '__main__':
    fptr = open("result.txt", 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)
    
        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
