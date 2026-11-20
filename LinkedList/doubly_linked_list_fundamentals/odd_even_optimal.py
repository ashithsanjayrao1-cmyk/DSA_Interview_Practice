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


def oddEven(head):

    if head is None or head.next is None:
        return head

    odd = head
    even = head.next

    evenHead = head.next


    while even is not None and even.next is not None:

        odd.next = odd.next.next 
        even.next = even.next.next

        odd = odd.next

        even = even.next

    odd.next = evenHead

    return head

def print_arr_to_linked_list(head):
    temp = head

    while temp is not None:
        print(temp.data,end=" -> ")

        temp = temp.next

    print("None")


arr = [1,3,4,2,5,6]

head = arr_to_linked_list(arr)
head = oddEven(head)

print_arr_to_linked_list(head)


