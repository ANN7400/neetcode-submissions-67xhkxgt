class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        left, right = dummy, dummy

        # advance right by n+1 steps (n steps ahead of left)
        for _ in range(n + 1):
            right = right.next

        # move both until right hits None
        while right:
            left = left.next
            right = right.next

        # delete the target node
        left.next = left.next.next

        return dummy.next 