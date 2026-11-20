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


def palindrome(head):

    if head is None or head.next is None:
        return True

    temp = head

    stack = []

    while temp is not None:

        stack.append(temp.data)
        temp = temp.next

    temp = head

    while temp is not None:
        if temp.data != stack[-1]:
            return False

        temp = temp.next
        stack.pop()

    return True




def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")


arr = [1,2,3,4,5]

head = arr_to_linked_list(arr)

print_linked_list(head)

head = palindrome(head)

print("Is Palindrome",head)






    