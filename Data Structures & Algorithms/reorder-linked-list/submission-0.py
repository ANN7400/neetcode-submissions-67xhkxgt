class Solution:
    def reorderList(self, head: ListNode) -> None:
        # Step 1: find middle using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is now at the middle

        # Step 2: reverse second half
        second = slow.next
        slow.next = None      # cut the list in half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # prev is now the head of the reversed second half

        # Step 3: merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2