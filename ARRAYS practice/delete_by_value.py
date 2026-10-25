class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node

def arr_to_linked_list(arr):
    n = len(arr)

    if not arr:
        return None

    head = Node(arr[0])

    mover = head

    for i in range(1,n):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

def delete_value(head,value):

    if head is None:
        return None

    if head.data == value:
        temp = head
        head = head.next

        return head

    temp = head
    prev = None

    while temp is not None:
        if temp.data == value:
            prev.next = temp.next

            break

        prev = temp
        temp = temp.next

    return head


def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end="-> ")

        temp = temp.next

    print("none")



arr = [12,5,8,7]

head = arr_to_linked_list(arr)

head = delete_value(head,8)

print_linked_list(head)