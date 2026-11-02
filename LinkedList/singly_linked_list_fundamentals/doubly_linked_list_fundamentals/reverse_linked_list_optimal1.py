class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node

def arr_to_linked_list(arr):
    n = len(arr)
    if not arr:
        return arr

    head = Node(arr[0])
    mover = head

    for i in range(1,n):
        temp = Node(arr[i],None)

        mover.next = temp
        mover = temp
    return head


def reverseLinke(head):

    temp = head

    prev = None

    while temp is not None:

        front = temp.next

        temp.next = prev

        prev = temp

        temp = front

    return prev






def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")

arr = [1,2,3,4,5]

head = arr_to_linked_list(arr)

head = reverseLinke(head)

print_linked_list(head)
    
    