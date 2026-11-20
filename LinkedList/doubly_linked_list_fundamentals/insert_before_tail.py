class Node:
    def __init__(self,data,next_node = None,prev = None):

        self.data = data 
        self.next = next_node
        self.prev = prev

def arr_to_doubly(arr):
    n = len(arr)

    if not arr:
        return arr

    head = Node(arr[0])

    back = head

    for i in range(1,n):
        temp = Node(arr[i],None,back)

        back.next = temp
        back = temp


    return head


def insert_before_tail(head,val):
    if head is None:
        return None

    if head.next is None:

        new_node = Node(val,head,None)
        head.prev = new_node
        return new_node

    tail = head
    while tail.next is not None:
        tail = tail.next

    prev_node = tail.prev

    new_node = Node(val,tail,prev_node)

    prev_node.next = new_node
    tail.prev = new_node

    return head


def print_doubly(head):
    temp = head
    while temp is not None:
        print(temp.data , end = " <-> ")

        temp = temp.next

    print("None")


arr = [12, 5, 8, 7]
head = arr_to_doubly(arr)

head = insert_before_tail(head, 100)

print_doubly(head)  
        