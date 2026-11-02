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


def removeNthNode(head,n):

    fast = head
    for i in range(n):
        fast = fast.next

    if fast is None:
        return head.next
    
    slow = head
     

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    delNode = slow.next
    slow.next = slow.next.next

    return head



def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")

arr = [1,2,3,4,5]

head = arr_to_linked_list(arr)

head = removeNthNode(head,5)

print_linked_list(head)
    
    