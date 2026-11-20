class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node

def arr_to_linked_list(arr):
    n = len(arr)
    if not arr:
        return arr

    head= Node(arr[0])

    mover = head

    for i in range(1,n):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head


def odd_even(head):

    ans = []

    temp = head

    while temp is not None and temp.next is not None:

        ans.append(temp.data)
        temp = temp.next.next


    if temp is not None:

        ans.append(temp.data)

    temp = head.next

    while temp is not None and temp.next is not None:

        ans.append(temp.data)
        temp = temp.next.next


    if temp is not None:
        ans.append(temp.data)

    i = 0
    temp = head
    while temp is not None:
        temp.data = ans[i]
        i+=1
        temp = temp.next

    return head


def print_linked_List(head):
    temp = head

    while temp is not None:


        print(temp.data,end=' -> ')
        temp = temp.next

    print("None")


arr = [1,3,4,2,5,6]

head = arr_to_linked_list(arr)
head = odd_even(head)

print_linked_List(head)








