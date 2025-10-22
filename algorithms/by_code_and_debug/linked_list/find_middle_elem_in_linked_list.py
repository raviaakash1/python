from linked_list import *

def find_middle(head, length_list):
    median = length_list // 2
    curr_index = 0
    while head:
        if median == curr_index:
            return head.val
        head = head.next
        curr_index += 1


# fast approach
def hare_tortoise(head):
    slow_ptr = head
    fast_ptr = head
    while  fast_ptr != None and fast_ptr.next != None :
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    return slow_ptr.val
        
if __name__ == "__main__":
    arr = [int(i)for i in input("Enter list array : ").split(" ")]
    new_list = SinglyLinkedList()
    for i in arr:
        new_list.append(i)
    list_length = new_list.linked_list_length()
    print(list_length)
    new_list.print()
    print("\n middle index value",hare_tortoise(new_list.head))
