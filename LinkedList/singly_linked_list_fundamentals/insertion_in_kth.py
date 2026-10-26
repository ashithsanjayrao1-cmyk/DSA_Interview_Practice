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
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head


def insert_kth_node(head,val,k):
    if head is None:
        if k==1:
            return Node(val)

        return head

    if k == 1:
        return Node(val,head)

    temp = head
    count = 0

    while temp is not None:
        count += 1

        if count == k-1:
            new_node = Node(val,temp.next)
            temp.next = new_node
            break
        temp = temp.next

    return head

def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = "-> ")
        temp = temp.next

    print("None")


arr = [12,5,8,7]
head= arr_to_linked_list(arr)

head = insert_kth_node(head,100,6)

print_linked_list(head)