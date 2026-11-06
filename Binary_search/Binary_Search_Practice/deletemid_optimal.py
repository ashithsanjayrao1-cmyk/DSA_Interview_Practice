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

        temp = Node(arr[i],None)
        mover.next = temp
        mover = temp

    return head


def DeleteNode(head):

    if head is None or head.next is None:
        return None
    

    slow = head
    fast = head

    fast = fast.next.next

    while fast is not None and fast.next is not None:

        slow = slow.next

        fast = fast.next.next

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

head = DeleteNode(head)
print_linked_list(head)





    