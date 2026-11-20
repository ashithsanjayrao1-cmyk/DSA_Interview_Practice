class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node

def arr_to_linked_list(arr):
    n = len(arr)
    if not arr:
        return arr
    head = Node(arr[0])

    mover = head

    for i in range(1,n):
        temp = Node(arr[i],None)
        mover.next = temp
        mover = temp

    return head

def collisionpoint(smallHead,largerHead,d):

    while d:

        d-=1
        largerHead = largerHead.next

    while smallHead != largerHead:

        smallHead = smallHead.next
        largerHead = largerHead.next

    return smallHead


def intersection(head1,head2):

    t1 = head1
    n1 = 0

    t2 = head2
    n2 = 0

    while t1 is not None:
        n1+=1
        t1 = t1.next

    while t2 is not None:
        n2+=1
        t2 = t2.next

    if n1 < n2:
        return collisionpoint(head1,head2,n2 - n1)

    else:
        return collisionpoint(head2,head1,n1-n2)







def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data,end=" -> ")
        temp = temp.next

    print("None")

head1 = arr_to_linked_list([3,1,4,6,2])
head2 = arr_to_linked_list([1,2,4,5,4,6,2])

head2.next.next = head1.next.next

intersect_node = intersection(head1,head2)

if intersect_node is not None:
    print("Intersection found at node with data:", intersect_node.data)
else:
    print("No intersection found.")

        



    



