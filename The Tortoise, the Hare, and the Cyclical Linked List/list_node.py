from __future__ import annotations
from typing import Optional


class ListNode:

    __slots__ = "value", "next_node"

    def __init__(self, value: Optional[int] = None, next_node: Optional[ListNode] = None):
        self.value = value
        self.next_node = next_node

    @classmethod
    def generateList(cls, length: int = 0, cycle: int = 0) -> tuple[Optional[ListNode], Optional[ListNode]]:
        """
        Creates a linked list of length [length]. The value attribute is an integer,
        beginning at 1 and proceeding in ascending order. A cycle parameter exists.
        If passed, this will set the next_node attribute of the final node to the
        1-indexed ListNode. Pass 0 to not incorporate a cycle. Returns a tuple
        of the form (root, cycle_beginning), where root is the ListNode with value
        property 1, and cycle_beginning is the next_node property of the final node.
        """
        nodes = [cls(val + 1) for val in range(length)]
        for i, node in enumerate(nodes):
            if i == len(nodes) - 1 and cycle:
                node.next_node = nodes[cycle - 1]
            elif i < len(nodes) - 1:
                node.next_node = nodes[i + 1]
        return (nodes[0], node.next_node) if nodes else (None, None)

    def __repr__(self) -> str:
        """
        Returns the nodes' values in order, separated by an arrow.
        Finished off with a None if the linked list is null-terminated;
        otherwise, the cycle's beginning is printed, followed by a (C).
        """
        node_set = set()
        stringified = ""
        while self is not None:
            if self not in node_set:
                stringified += f"{self.value} -> "
                node_set.add(self)
                self = self.next_node
            else:
                return stringified + f"{self.value} (C)"
        return stringified + "None"
