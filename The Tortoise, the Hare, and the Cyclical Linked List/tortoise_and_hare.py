from typing import Optional
from list_node import ListNode


def tortoise_and_hare_bool(head: Optional[ListNode]) -> bool:
    """
    Implementation of the tortoise and hare algorithm.
    Returns True or False based upon whether a cycle exists.
    """
    fast = slow = head
    while fast and fast.next_node:
        slow, fast = slow.next_node, fast.next_node.next_node
        if slow == fast:
            return True
    return False


def tortoise_and_hare(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Implementation of the tortoise and hare algorithm.
    If no cycle is found, None is returned.
    Otherwise, the node where the cycle began is returned.
    """
    fast = slow = head
    while fast and fast.next_node:
        slow, fast = slow.next_node, fast.next_node.next_node
        if fast == slow:
            while head != slow:
                head, slow = head.next_node, slow.next_node
            return head
