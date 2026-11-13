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

def findmiddle(head):
    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next

    return slow

def merge2(list1,list2):
    dummy_node = Node(-1)
    res = dummy_node

    while list1 is not None and list2 is not None:
        if list1.data < list2.data:
            res.next = list1
            res = list1
            list1 = list1.next

        else:

            res.next = list2
            res = list2
            list2 = list2.next
    if list1:
        res.next = list1

    else:
        res.next = list2
    return dummy_node.next


def sortLinked_list(head):
    if head is None or head.next is None:
        return head


    middle = findmiddle(head)

    lefthead = head
    righthead = middle.next


    middle.next = None

    lefthead = sortLinked_list(lefthead)
    righthead = sortLinked_list(righthead)

    return merge2(lefthead,righthead)

def print_linked_list(head):
    temp = head
    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.next

    print("None")




arr = [4, 2, 8, 5, 1, 3, 7]
head = arr_to_linked_list(arr)

print("Original list:")
print_linked_list(head)

sorted_head = sortLinked_list(head)

print("\nSorted list (Merge Sort):")
print_linked_list(sorted_head)