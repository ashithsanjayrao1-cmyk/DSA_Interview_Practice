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

def reverse(head):

    if head is None or head.next is None:
        return head
    

    newHead = reverse(head.next)
    front = head.next 
    front.next = head
    head.next = None
    return newHead



def palindrome(head):

    if head is None or head.next is None:
        return True

    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:

        slow = slow.next
        fast = fast.next.next

    newHead = reverse(slow.next)

    first = head
    second = newHead

    while second is not None:

        if first.data != second.data:
            reverse(newHead)
            return False
        first = first.next

        second = second.next

    reverse(newHead)
    return True


def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")


arr = [1,2,3,3,2,1]

head = arr_to_linked_list(arr)

print_linked_list(head)

head = palindrome(head)

print("Is Palindrome",head)






    