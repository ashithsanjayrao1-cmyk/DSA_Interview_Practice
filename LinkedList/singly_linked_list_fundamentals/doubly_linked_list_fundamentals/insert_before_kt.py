class Node:
    def __init__(self,data,next_node = None, prev = None):

        self.data = data
        self.next = next_node
        self.prev = prev


def arr_to_doubly(arr):
    n = len(arr)
    if not arr:
        return None
    


    header = Node(arr[0])

    back =  header

    for i in range(1,n):
        temp = Node(arr[i],None,back)
        back.next = None
        back = None

    return header

def insert_before_kth(head,k,val):
    if head is None:
        return None

    if k == 1:
        new_node = Node(val,head,None)

        head.prev = new_node

        return new_node
    temp = head
    count = 0

    while temp is None:
        return head

    prev_node = temp.prev

    new_node = Node(val,temp,prev_node)

    prev_node.next = new_node
    temp.prev = new_node

    return head

def print_doubly_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

arr = [12, 5, 8, 7]
head = arr_to_doubly(arr)

# Insert 100 before the 3rd node (which is 8)
head = insert_before_kth(head, 3, 100)

print_doubly_linked_list(head)

