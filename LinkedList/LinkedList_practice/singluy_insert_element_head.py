class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node
def arr_to_linked_list(arr):
    if not arr:
        return None

    n = len(arr)

    head = Node(arr[0])
    mover = head

    for i in range(1,n):
        temp = Node(arr[i],None)
        mover.next = temp
        mover = temp
    return head

def insertHead(head,x):
    temp = Node(x)
    temp.next = head

    return temp


def print_linked_list(head):
    temp = head

    while temp is not None:
        print(temp.data,end="-> ")

        temp = temp.next                    

    print("None")


arr = [12,5,8,7]

head_node = arr_to_linked_list(arr)

print("Original")
print_linked_list(head_node)

head_node = insertHead(head_node,11)

print("After Deleting:")
print_linked_list(head_node)

