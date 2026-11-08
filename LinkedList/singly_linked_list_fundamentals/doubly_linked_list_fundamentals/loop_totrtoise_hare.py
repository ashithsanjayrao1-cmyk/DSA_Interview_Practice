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


def detectLoop(head):

    slow = head
    fast = head

    while fast.next is not None and fast is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False







def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")


head = arr_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])

target_node = head.next.next

tail = head

while tail.next is not None:
    tail = tail.next

tail.next = target_node

print("Has loop:", detectLoop(head))