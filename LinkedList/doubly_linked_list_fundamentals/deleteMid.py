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


def DeleteNode(head):

    temp = head
    cunt = 0

    if head is None or head.next is None:

        return None
    

    while temp is not None:

        cunt += 1

        temp = temp.next

    res = cunt//2

    temp = head

    while temp is not None:

        res -=1


        if res == 0:
            middle = temp.next
            temp.next = temp.next.next  

            break

        temp = temp.next

    return head

def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")


arr = [1,2,3,4,5]

head = arr_to_linked_list(arr)

head = DeleteNode(head)
print_linked_list(head)





    