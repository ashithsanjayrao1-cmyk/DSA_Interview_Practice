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

        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

def add_2_number(head1,head2):

    t1 = head1
    t2 = head2

    dummy = Node(-1)

    curr = dummy

    carry = 0

    while t1 is not None or t2 is not None or carry > 0:

        sum = carry

        if t1 is not None:
            sum += t1.data

            t1 = t1.next

        if t2 is not None:
            sum += t2.data

            t2 = t2.next

        carry = sum //10

        new_node = Node(sum % 10)

        curr.next = new_node
        curr = curr.next

    return dummy.next

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


arr1 = [2, 4, 3]
arr2 = [5, 6, 4]

head1 = arr_to_linked_list(arr1)
head2 = arr_to_linked_list(arr2)

result_head = add_2_number(head1, head2)

print_linked_list(result_head)



    
        