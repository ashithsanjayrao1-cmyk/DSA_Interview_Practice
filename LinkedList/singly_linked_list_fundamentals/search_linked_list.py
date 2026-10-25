class Node:
    def __init__(self,data,next_node=None):

        self.data = data
        self.next = next_node

def arr_to_linked_list(arr):

    n = len(arr)
    if not arr:
        return None

    head = Node(arr[0])
    mover = head

    for i in range(1,n):

        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

def search(head,target):
    temp = head

    while temp is not None:
        if temp.data == target:
            return True
        temp = temp.next


    return False

arr = [12,5,7,8]

head = arr_to_linked_list(arr)

print(search(head,5))

