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

def findKthNode(temp,k):

    k-=1
    while temp is not None and k>0:
        k-=1
        temp = temp.next

    return temp

def reverse(head):
    if head is None or head.next is None:
        return head

    newHead = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newHead


def reverseKth_node(head,k):

    temp = head
    prev_node = None

    while temp is not None:

        kthNode = findKthNode(temp,k)

        if kthNode is None:

            if prev_node:

                prev_node.next = temp
                                   

            break

        next_node = kthNode.next

        kthNode.next = None

        reverse(temp)


        if temp == head:

            head = kthNode

        else:
            prev_node.next = kthNode

        prev_node = temp

        temp = next_node

    return head

                         
def print_linked(head):

    temp = head

    while temp is not None:
        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
head = arr_to_linked_list(arr)

print("Original list:")
print_linked(head)

k = 3
head = reverseKth_node(head, k)

print(f"\nList after reversing in groups of {k}:")
print_linked(head)


