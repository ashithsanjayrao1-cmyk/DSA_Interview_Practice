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

    map = {}

    temp = head

    while temp is not None:

        if temp in map:

            return temp
        map[temp] = 1

        temp = temp.next

    return None




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

loop_start = detectLoop(head)

if loop_start is not None:

    print("Loop detected! It starts at node with data:", loop_start.data)
else:
    print("No loop detected.")

