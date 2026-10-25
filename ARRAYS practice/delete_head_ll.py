class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node

def arr_to_linked_list(arr):
    n = len(arr)
    if not arr:
        return 0

    head = Node(arr[0])

    mover = head

    for i in range(n):

        temp = Node(arr[i])

        mover.next = temp

        mover = temp

    return head


def delete_head(head):
    if head is None:
        return None


    temp = head
    head= head.next

    return head

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data,end="-> ")
        temp = temp.next
    print("None")



arr = [12,5,8,7]
head = arr_to_linked_list(arr)

print("Original linked_list")

print_linked_list(head)

head = delete_head(head)

print("After Deleting head")
print_linked_list(head)