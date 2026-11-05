class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node

def arr_to_linked_list(arr):
    if not arr:
        return None
    n = len(arr)

    head = Node(arr[0])
    mover = head

    for i in range(1,n):

        temp = Node(arr[i],None)
        mover.next = temp 
        mover = temp

    return head

def middle(head):

    slow = head
    fast = head


    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

    return slow


def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")


arr = [1,2,3,4,5,6]


node = arr_to_linked_list(arr)

result = middle(node)

print_linked_list(result)


 
