class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self) -> None:
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.next
        print()

    def insert(self, position: int, value: int) -> None:
        if position < 0:
            print("Invalid position")
            return

        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.head
        for _ in range(position - 1):
            if not node:
                print("Position out of bounds")
                return
            node = node.next

        if not node:
            print("Position out of bounds")
            return

        new_node.next = node.next
        node.next = new_node

    def delete(self, position: int) -> None:
        if position < 0 or not self.head:
            print("Invalid position")
            return

        if position == 0:
            self.head = self.head.next
            return

        node = self.head
        for _ in range(position - 1):
            if not node.next:
                print("Position out of bounds")
                return
            node = node.next

        if not node.next:
            print("Position out of bounds")
            return

        node.next = node.next.next

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = new_node


def unknown_command(*args, **kwargs):
    print("Command not found!")

def build_dispatcher(linked_list: LinkedList):
    return {
        1: lambda pos, val: linked_list.insert(pos, val),
        2: lambda pos: linked_list.delete(pos),
        3: lambda: linked_list.traverse(),
        4: lambda val: linked_list.append(val)
    }

def dispatch(opt_dict, command, *args, **kwargs):
    func = opt_dict.get(command, unknown_command)
    return func(*args, **kwargs)

def call_res_function(linked_list: LinkedList, s_option: int, opt_dict: dict):
    if s_option == 1:
        pos = int(input("Enter position > "))
        val = int(input("Enter value > "))
        dispatch(opt_dict, s_option, pos, val)
    elif s_option == 2:
        pos = int(input("Enter position to delete > "))
        dispatch(opt_dict, s_option, pos)
    elif s_option == 3:
        dispatch(opt_dict, s_option)
    elif s_option == 4:
        val = int(input("Enter value to append > "))
        dispatch(opt_dict, s_option, val)
    else:
        dispatch(opt_dict, s_option)
        sys.exit(0)

    print("Updated list:")
    linked_list.traverse()

def options() -> int:
    menu = '''
        Insert : 1
        Delete : 2
        Traverse : 3
        Append : 4
    '''
    return int(input(menu + "\nChoose an operation >> "))

if __name__ == "__main__":
    ll = LinkedList()
    for val in [4, 5, 10, 15]:
        ll.append(val)

    print("Initial linked list:")
    ll.traverse()

    s_option = options()
    opt_dict = build_dispatcher(ll)
    call_res_function(ll, s_option, opt_dict)