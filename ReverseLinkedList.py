# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        while head:
            l += [head.val]
            head = head.next
        res = ListNode(0)
        answer = res
        for i in reversed(l):
            res.next = ListNode(i)
            res = res.next
        return answer.next
