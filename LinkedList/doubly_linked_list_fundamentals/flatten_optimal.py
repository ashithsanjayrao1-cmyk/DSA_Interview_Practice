class Node:
    def __init__(self,data,next_node = None,child_node = None):

        self.data = data
        self.next = next_node
        self.child = child_node

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

def convert(arr):
    n = len(arr)

    if not arr:
        return None
    head = Node(arr[0])
    mover = head

    for i in range(1,n):

        new_node = Node(arr[i])
        mover.child = new_node
        mover = mover.child

    return head

def sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  

def MergeLists(list1,list2):

    dummy_node = Node(-1)

    res = dummy_node

    while list1 is not None and list2 is not None:

        if list1.data < list2.data:

            res.child = list1
            res = list1
            list1 = list1.child

        else:


            res.child = list2
            res = list2
            list2 = list2.child

        res.next = None

    if list1:

        res.child = list1

    else:

        res.child = list2

    return dummy_node.child





    

def print_linked_list(head):


    temp = head

    while temp is not None:

        print(temp.data,end = " -> ")
        temp = temp.child

    print("None")


# Level 1 (Main next pointers)
head = Node(5)
head.next = Node(10)
head.next.next = Node(19)
head.next.next.next = Node(28)

# Level 2 (Child pointers for 5)
head.child = Node(7)
head.child.child = Node(8)
head.child.child.child = Node(30)

# Level 2 (Child pointers for 10)
head.next.child = Node(20)

# Level 2 (Child pointers for 19)
head.next.next.child = Node(22)
head.next.next.child.child = Node(50)

# Level 2 (Child pointers for 28)
head.next.next.next.child = Node(35)
head.next.next.next.child.child = Node(40)

print("Flattening and sorting the multi-level linked list...")
flattened_head = MergeLists(head)

print("Flattened List:")
print_linked_list(flattened_head)