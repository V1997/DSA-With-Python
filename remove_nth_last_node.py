

# Remove nth node from the end from a linked list.

def remove_nth_last_node(head, n):

    right = head
    left = head
    
    for i in range(n):
        right = right.next

    if not right:
        return head.next
    
    while right.next:
        right = right.next
        left = left.next

    left.next = left.next.next

    return head

