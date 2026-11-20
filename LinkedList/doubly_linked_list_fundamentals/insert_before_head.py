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


def insert_before_head(head,val):
    new_node = Node(val,head,None)

    if head is not None:
        head.prev = new_node


    return new_node



def print_doubly_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " <-> ")
        temp = temp.next

    print("None")


arr = [12,5,8,7]
head = arr_to_doubly_linked_list(arr)

head = insert_before_head(head,100)

print_doubly_linked_list(head)