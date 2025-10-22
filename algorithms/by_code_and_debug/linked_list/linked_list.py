class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def insert(self, val, index):
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            indx_counter = 0
            curr = self.head
            while curr.next != None:
                if indx_counter + 1 == index:
                    new_node.next = curr.next
                    curr.next = new_node
                    return
                curr = curr.next
                indx_counter += 1
            if indx_counter + 1 == index:
                curr.next = new_node
            else:
                print("Invalid Index !!!!!")
            
    def delete(self, index):
        if index == 0:
            curr_node = self.head
            self.head = self.head.next
            del curr_node
        else:
            indx_counter = 0
            curr = self.head
            while curr != None:
                
                if indx_counter + 1 == index:
                    
                    if curr.next.next == None:
                        curr.next = None
                    else:
                        curr.next = curr.next.next
                    return
                curr = curr.next
                indx_counter += 1
                
    def linked_list_length(self):
        length = 0
        curr = self.head
        while curr:
            curr = curr.next
            length += 1
        return length


    def reverse(self):
        curr = self.head
        temp = None
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev   = curr
            curr = temp

        
        self.head = prev



    def print(self):
        curr = self.head
        while curr:
            print(curr.val,end=" ")
            curr = curr.next

if __name__ == "__main__":
    single_linked_list = SinglyLinkedList()
    single_linked_list.append(10)
    single_linked_list.append(211)
    single_linked_list.append(4)
    single_linked_list.insert(1,0)
    
    single_linked_list.insert(2,3)
    single_linked_list.insert(5,2)
    single_linked_list.insert(15,6)
    # single_linked_list.print()
    single_linked_list.delete(3)
    single_linked_list.print()
    single_linked_list.reverse()
    print()
    single_linked_list.print()