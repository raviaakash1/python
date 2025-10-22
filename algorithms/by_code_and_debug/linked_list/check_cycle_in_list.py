class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CyclicSinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to itself to start the cycle
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head  # Maintain the cycle

    def print(self, count):
        curr = self.head
        printed = 0
        while curr and printed < count:
            print(curr.val, end=" ")
            curr = curr.next
            printed += 1
        print()

    def if_cyclic(self):
        dict_address = {}
        curr = self.head

        while curr != None:
            if curr in dict_address.keys() and dict_address[curr] == curr.val:
                return True
            else:
                if curr not in dict_address.keys():
                    dict_address[curr] = curr.val
            curr = curr.next
    def floyd_cycle_detection(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
# Example usage
if __name__ == "__main__":
    clist = CyclicSinglyLinkedList()
    clist.append(10)
    clist.append(20)
    clist.append(30)
    clist.append(40)

    clist.print(10) 
    print(clist.floyd_cycle_detection())
