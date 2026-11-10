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

def merge(head1,head2):

    arr = []
    temp1 = head1
    temp2 = head2

    while temp1 is not None:

        arr.append(temp1.data)

        temp1 = temp1.next

    while temp2 is not None:
        arr.append(temp2.data)
        temp2 = temp2.next

    arr.sort()

    head = arr_to_linked_list(arr)

    return head




def print_linked_list(head):


    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")


head1 = arr_to_linked_list([2, 4, 8, 10])
head2 = arr_to_linked_list([1, 3, 3, 6, 11, 14])

print("List 1:")
print_linked_list(head1)

print("\nList 2:")
print_linked_list(head2)

merged_head = merge(head1, head2)

print("\nMerged and Sorted List:")
print_linked_list(merged_head)