# Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Tortoise-hare, with entry point

def tortoiseHare(head):
    if not head:
        return None

    slow = head
    fast = head

    # First, detect if a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Cycle detected — find the entry point
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  

    return None  # No cycle found



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

entry = tortoiseHare(a)
print(f"example 1: cycle entry = {entry.val if entry else None}")  # should be 2


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

entry = tortoiseHare(a)
print(f"example 2: cycle entry = {entry.val if entry else None}")  # should be None
