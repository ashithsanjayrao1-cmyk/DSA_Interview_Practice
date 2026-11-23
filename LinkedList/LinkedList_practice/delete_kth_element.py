class Node:
    def __init__(self,data,next_node = None,prev_node = None):

        self.data = data
        self.next = next_node
        self.prev = prev_node
def arr_to_doubly(arr):

    n = len(arr)
    if not arr:
        return None

    head = Node(arr[0])
    back = head


    for i in range(1,n):

        temp = Node(arr[i],None,back)
        back.next = temp
        back = temp

    return head


def deletekthElement(head,k):

    if head is None:
        return None

    temp = head
    count = 0


    while temp is not None:
        count += 1

        if count == k:
            break

        temp = temp.next

    if temp is None:
        return head

    back_node = temp.prev

    front_node = temp.next

    if back_node is None and front_node is None:
        return None

    elif back_node is None:

        head = front_node
        head.prev = None
        temp.next = None
        return head
    elif front_node is None:

        back_node.next = None
        temp.prev = None
        return head
    else:

        back_node.next = front_node
        front_node.prev = back_node

        temp.next = None
        temp.prev = None
        return head
def print_dll(head):
    curr = head
    res = []
    while curr:
        res.append(str(curr.data))
        curr = curr.next
    print(" <-> ".join(res))

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    
    # 1. Convert array to DLL
    head = arr_to_doubly(arr)
    print("Original DLL:")
    print_dll(head)
    
    # 2. Delete the 3rd element (which is 30)
    print("\nDeleting 3rd element:")
    head = deletekthElement(head, 3)
    print_dll(head)


    
