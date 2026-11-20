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


def removeNthNode(head,n):

    count = 0
    temp = head

    while temp is not None:

        count += 1

        temp = temp.next

    if count == n:

        newHead = head.next
        return newHead

    res = count - n
    temp = head

    while temp is not None:
        res -= 1

        if res == 0:
            break
        temp = temp.next

        if n == 0:
            return head

    delNode = temp.next
    temp.next = temp.next.next

    return head

    




def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")

arr = [1,2,3,4,5]

head = arr_to_linked_list(arr)

head = removeNthNode(head,4)

print_linked_list(head)
    
    