class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node


def arr_yto_linked_list(arr):

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




def insert_before_value(head,val,before_val):
    if head is None:
        return None

    if head.data == before_val:
        return Node(val,head)

    temp = head

    while temp.next is not None:
        if temp.next.data == before_val:
            new_node = Node(val,temp.next)

            temp.next = new_node

            break
        temp = temp.next

    return head


def print_linked_list(head):
    temp = head

    while temp is not None:
        print(temp.data,end="-> ")
        temp = temp.next


    print("None")


arr = [12,5,8,7]

head = arr_yto_linked_list(arr)

head = insert_before_value(head,100,8)

print_linked_list(head)
