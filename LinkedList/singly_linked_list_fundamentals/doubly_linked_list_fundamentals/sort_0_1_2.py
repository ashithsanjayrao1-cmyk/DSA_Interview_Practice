class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node

def arr_to_linked_list(arr):
    n= len(arr)

    if not arr:
        return arr


    head = Node(arr[0])
    mover = head

    for i in range(1,n):
        temp = Node(arr[i],None)
        mover.next = temp
        mover = temp

    return head


def sort012(head):

    count0 = 0
    count1 = 0
    count2 = 0

    temp = head

    while temp is not None:

        if temp.data == 0:
            count0 +=1 

        elif temp.data == 1:
            count1 += 1

        else:
            count2 += 1

        temp = temp.next

    temp = head

    while temp is not None:

        if count0:
            temp.data = 0
            count0 -=1

        elif count1:
            temp.data = 1
            count1 -= 1
        else:
            temp.data = 2
            count2 -= 1

        temp = temp.next

    return head

def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end=" -> ")

        temp = temp.next

    print("None")

arr = [1,0,1,2,0,2,1]

head = arr_to_linked_list(arr)
head = sort012(head)

print_linked_list(head)


    


        

