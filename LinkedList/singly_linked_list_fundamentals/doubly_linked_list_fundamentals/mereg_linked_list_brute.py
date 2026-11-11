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

def sorting(head):

    if head is None:
        return head
    
    temp = head
    arr = []

    while temp is not None:

        arr.append(temp.data)
        temp = temp.next

    arr.sort()

    i = 0 
    temp = head

    while temp is not None:

        temp.data = arr[i]
        i +=1

        temp = temp.next

    return head


def print_linked_list(head):

    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next


    print("None")

head = arr_to_linked_list([4, 2, 8, 5, 1])

print("Original list:")
print_linked_list(head)

sorted_head = sorting(head)

print("\nSorted list:")
print_linked_list(sorted_head)




