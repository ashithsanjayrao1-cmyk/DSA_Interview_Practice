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

def findLength(slow, fast):
    count = 1

    fast = fast.next

    while slow is not fast:
        count+=1
        fast = fast.next
    return count


def lengthLoop(head):

    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return findLength(slow,fast)

    return 0

def print_linked(head):

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

loop_length = lengthLoop(head)
print("Length of the loop is:", loop_length)


