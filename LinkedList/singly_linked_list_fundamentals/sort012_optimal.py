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


def sorting012(head):

    zeroHead = Node(-1)
    oneHead = Node(-1)
    twoHead = Node(-1)

    zero = zeroHead
    one = oneHead
    two = twoHead

    temp = head

    while temp is not None:

        if temp.data == 0:
            zero.next = temp
            zero = temp

        elif temp.data == 1:
            one.next = temp
            one = temp

        else:

            two.next = temp
            two = temp

        temp = temp.next


    zero.next = oneHead.next if oneHead.next else twoHead.next

    one.next = twoHead.next

    two.next = None

    newHead = zeroHead.next

    return newHead

def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end=" -> ")

        temp = temp.next

    print("None")

arr = [1,0,1,2,0,2,1]

head = arr_to_linked_list(arr)
head = sorting012(head)

print_linked_list(head)




                          

