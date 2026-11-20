class Node:
    def __init__(self,data,next_node = None,back = None):

        self.data = data
        self.next = next_node
        self.back = back

def arr_to_doubly_linked_list(arr):
    if not arr:
        return None

    n = len(arr)


    head = Node(arr[0])
    back = head


    for i in range(1,n):
        temp = Node(arr[i],None,back)
        back.next = temp
        back = temp

    return head


def delete_kth_node(head,k):

    if head is None:
        return None

    temp = head
    count = 0

    while temp is not None:
        count+=1
        if count == k:
            break
        temp = temp.next


    if temp is None:
        return head

    back_node = temp.back
    front_node =temp.next

    if back_node is None and front_node is None:
        return None

    elif back_node is None:
        head = front_node
        head.back = None
        temp.next = None
        return head

    elif front_node is None:
        back_node.next = None
        temp.back = None
        return head

    else:
        back_node.next = front_node
        front_node.back = back_node

        temp.next = None
        temp.back = None

        return head


def print_doublyy_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data,end= " <-> ")
        temp = temp.next

    print("None")



arr = [12,5,8,7]

head = arr_to_doubly_linked_list(arr)

head = delete_kth_node(head,3)

print_doublyy_linked_list(head)
