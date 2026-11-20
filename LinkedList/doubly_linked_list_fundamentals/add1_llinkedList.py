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


def reverse(head):

    if head is None or head.next is None:
        return head

    new_head = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None

    return new_head


def add1(head):

    head = reverse(head)

    temp = head
    carry = 1

    while temp is not None:

        temp.data = temp.data + carry

        if temp.data < 10:
            carry = 0
            break
        else:
            temp.data = 0

            carry = 1

        temp = temp.next

    if carry == 1:
        newNode = Node(1)


        head = reverse(head)
        newNode.next = head
        return newNode

    head = reverse(head)
    return head

def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")


arr = [1,9,5,9]

node = arr_to_linked_list(arr)

result = add1(node)

print_linked_list(result)


 
