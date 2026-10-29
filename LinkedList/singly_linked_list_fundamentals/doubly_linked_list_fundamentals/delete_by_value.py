class Node:
    def __init__(self,data,next_node = None,prev = None):

        self.data = data
        self.next = next_node
        self.back = prev


def arr_to_doubly_linked_list(arr):

    n = len(arr)

    if not arr:
        return None

    head = Node(arr[0])
    back = head

    for i in range(1,n):
        temp = Node(arr[i],None,back)
        back.next = temp
        back = temp

    return head


def delet_by_value(temp):

    back_node = temp.back
    front_node = temp.next

    if back_node is not None:
        back_node.next = front_node

    if front_node is not None:
        front_node.back = back_node

    temp.next = None
    temp.back = None

def print_doubly_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data,end = " <-> ")

        temp = temp.next

    print("None")


arr = [12,5,8,7]

head = arr_to_doubly_linked_list(arr)

node_to_delete = head.next

delet_by_value(node_to_delete)

print_doubly_linked_list(head)
