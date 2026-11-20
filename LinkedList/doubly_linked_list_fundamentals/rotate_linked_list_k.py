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

def findNthNode(temp,k):

    cnt = 1
    while temp is not None:
        if cnt == k:
            return temp
        cnt += 1

        temp = temp.next

    return temp 


def rotatedK(head,k):
    if head is None or k == 0:
        return head
    
    len = 1
    tail = head

    while tail.next is not None:
        len += 1
        tail = tail.next

    if k % len == 0:
        return head
    k = k % len

    tail.next = head

    new_tail = findNthNode(head,len-k)

    head = new_tail.next

    new_tail.next = None

    return head

def print_linked_list(head):

    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")


arr = [1, 2, 3, 4, 5]
head = arr_to_linked_list(arr)

print("Original list:")
print_linked_list(head)

k = 2
head = rotatedK(head, k)

print(f"\nList after rotating by {k} places:")
print_linked_list(head)
