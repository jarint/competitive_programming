# detects if a cycle exists without returning the entry point of the cycle

# Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Tortoise-hare, no entry point
def hasCycle(head):
    if not head:
        return False
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# setup example 1 - has cycle

# 1 → 2 → 3 → 4
#       ↑     ↓
#       ← ← ←

# Node 4 points back to Node 2

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = b # cycle

print(F"example 1: {hasCycle(a)}") 


# Setup example 2 - No cycle

# 1 → 2 → 3 → 4 → None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = None # Null ptr

print(F"example 2: {hasCycle(a)}") 
