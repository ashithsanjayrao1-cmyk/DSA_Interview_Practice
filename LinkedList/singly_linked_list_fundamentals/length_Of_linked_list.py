class Node():
    def __init__(self,data,next_node = None ):

        self.data = data
        self.next = next_node


def arr_to_linked_list(arr):
    if not arr:
        return None
    n = len(arr)

    head = Node(arr[0])
    mover = head


    for i in range(1,n):

        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head


def length_of_linked_list(head):
    temp = head
    count = 0

    while temp is not None:
        count += 1
        temp = temp.next

    return count

arr = [12,5,8,7]

head = arr_to_linked_list(arr)

print(length_of_linked_list(head))