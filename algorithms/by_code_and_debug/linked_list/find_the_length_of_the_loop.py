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

def find_loop_length(self):
    slow_ptr = self.head
    fast_ptr = self.head

    # Step 1: Detect cycle
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            # Step 2: Measure loop length
            count = 1
            temp = slow_ptr.next
            while temp != slow_ptr:
                count += 1
                temp = temp.next
            return count
    return 0  # No cycle
            

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
    print(clist.find_loop_length())
