# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        # Copy the next node's value into the current node
        node.val = node.next.val
        # Skip the next node
        node.next = node.next.next
