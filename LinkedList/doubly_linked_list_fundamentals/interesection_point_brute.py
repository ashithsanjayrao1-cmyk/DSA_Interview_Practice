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

def intersection(head1,head2):

    map = {}

    temp1 = head1

    while temp1 is not None:

        map[temp1] = 1
        temp1 = temp1.next

    temp2 = head2

    while temp2 is not None:
        if temp2 in map:
            return temp2

        temp2 = temp2.next

    return None

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data,end=" -> ")
        temp = temp.next

    print("None")

head1 = arr_to_linked_list([3,1,4,6,2])
head2 = arr_to_linked_list([1,2,4,5,4,6,2])

head2.next.next = head1.next.next

intersect_node = intersection(head1,head2)

if intersect_node is not None:
    print("Intersection found at node with data:", intersect_node.data)
else:
    print("No intersection found.")

        



    



