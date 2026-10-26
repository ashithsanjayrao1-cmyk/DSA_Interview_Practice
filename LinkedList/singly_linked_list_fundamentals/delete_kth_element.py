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

        temp = Node(arr[i])
        mover.next = temp 
        mover = temp

    return head

def delete_kth_node(head,k):
    if head is None:
        return None

    if k==1:

        temp = head
        head = head.next
        return head
    
    temp = head
    count = 0
    prev = None


    while temp is not None:
        count +=1
        if count == k:
            prev.next = prev.next.next
            break

        prev = temp
        temp = temp.next

    return head

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data,end ="-> ")
        temp = temp.next

    print("None")




arr = [12,5,8,7]

head_node = arr_to_linked_list(arr)

head_node = delete_kth_node(head_node,3)

print_linked_list(head_node)

