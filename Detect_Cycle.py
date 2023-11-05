



def detect_cycle(head):
    if head is None:
        return False
    
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

        if slow == fast:
            return True
    
    return False
