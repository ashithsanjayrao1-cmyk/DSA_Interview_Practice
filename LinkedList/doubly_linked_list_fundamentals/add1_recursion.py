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


def helper(head):

    temp = head

    if temp is None:
        return 1

    carry = helper(temp.next)

    temp.data = temp.data + carry

    if temp.data < 10:

        return 0
    else:

        temp.data = 0
        return 1
    
def add1(head):

        carry = helper(head)

        if carry == 1:
            newNode = Node(1)
            newNode.next = head
            return newNode
 
        return head


def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")


arr = [0,9,9,9]

node = arr_to_linked_list(arr)

result = add1(node)

print_linked_list(result)


 
