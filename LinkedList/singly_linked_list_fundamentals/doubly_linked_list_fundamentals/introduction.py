class Node:
    def __init__(self,data,next_node = None,back = None):

        self.data = data
        self.next = next_node
        self.back = back


def arr_to_doubly_linked_list(arr):
    n = len(arr)

    if not arr:
        return arr


    head = Node(arr[0])
    back = head

    for i in range(1,n):
        temp = Node(arr[i],None,back)
        back.next = temp
        back = temp

    return head

def print_doubly_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data,end=" <-> ")
        temp = temp.next

    print("None")

arr = [12, 5, 8, 7]
head = arr_to_doubly_linked_list(arr)
print_doubly_linked_list(head)