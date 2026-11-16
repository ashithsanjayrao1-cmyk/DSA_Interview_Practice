class Node:
    def __init__(self,data,next_node = None,prev = None):

        self.data = data
        self.next = next_node
        self.prev = prev


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


def removeDuplicates(head):
    temp = head

    while temp is not None:
        next_node = temp.next

        while next_node is not None and next_node.data == temp.data:

            next_node = next_node.next

        temp.next = next_node
        if next_node:
            next_node.prev = temp
        temp = temp.next

    return head


def print_doubly_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data,end = " <-> ")

        temp = temp.next

    print("None")


arr = [1,1,1,2,3,3,4]

head = arr_to_doubly_linked_list(arr)

node_to_delete = head.next

head = removeDuplicates(node_to_delete)

print_doubly_linked_list(head)
