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
    temp = head
    count = 0

    while temp is not None:

        count += 1

        temp = temp.next

    mid_node = (count//2) +1

    temp = head

    while temp is not None:

        mid_node = mid_node - 1

        if mid_node == 0: 
            break

        temp = temp.next

    return temp



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


 
