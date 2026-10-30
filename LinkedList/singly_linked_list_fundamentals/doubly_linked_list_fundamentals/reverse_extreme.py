class Node:
    def __init__(self,data,next_node = None,prev = None):

        self.data = data
        self.next = next_node
        self.prev = prev

def arr_to_doubly_linked_list(arr):
    n = len(arr)
    if not arr:
        return None


    head = Node(arr[0])
    back = head


    for i in range(1,n):

        temp = Node(arr[i],None,back)
        back.next = temp
        back = temp


    return head

def reverse_dll(head):

    if head is None or head.next is None:
        return head

    temp = head
    stack = []

    while temp is not None:

        stack.append(temp.data)
        temp = temp.next

    temp = head

    while temp is not None:
        temp.data = stack.pop()
        temp = temp.next

    return head

def print_doubly_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")


arr = [12, 5, 8, 7]
head = arr_to_doubly_linked_list(arr)
head = reverse_dll(head)
print_doubly_linked_list(head)
