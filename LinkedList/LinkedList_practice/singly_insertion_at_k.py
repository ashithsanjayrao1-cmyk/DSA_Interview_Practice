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

def insertK(head,x,k):

    if head is None:
        if k == 1:
            return Node(x)
        return head
    
    

    if k == 1:
        temp = Node(x,head)
        return temp
      

    temp = head
    count = 0

    while temp is not None:
        count += 1

        if count == k-1:

            new_node = Node(x)
            new_node.next = temp.next
            temp.next = new_node

            break

        temp = temp.next

    return head






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

head_node = insertK(head_node,4,3)

print("After Deleting:")
print_linked_list(head_node)

